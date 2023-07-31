import * as http from "http";
import { createProxy } from "http-proxy";
import detect from "detect-port";
import { readFileSync } from "fs";

const proxy = createProxy();
proxy.on("error", (err, req, res) => {
  console.log("#1", err);
  if (res && res.end) {
    res.end();
  }
  return;
});

const proxyHost = http.createServer(async (req: any, res: any) => {

  const result = /^(\d+)-.*$/.exec(req.headers.host)
  if (!result) {
    res.writeHead(400, { "Content-Type": "text/html" });
    res.end(
      readFileSync(
        __dirname + "/../templates/invalid-port-format.html",
        "utf-8"
      )
    );
    return;
  }

  const port = Number(result[1])

  switch (true) {
    case await detect(port) === port: {
      res.writeHead(404, { "Content-Type": "text/html" });
      res.end(
        readFileSync(
          __dirname + "/../templates/port-not-in-use.html",
          "utf-8"
        ).replace(/{{PORT}}/g, String(port))
      );
      return;
    }
    default: {
      proxy.web(req, res, {
        target: `http://localhost:${port}${req.url}`,
        ignorePath: true,
      });
    }
  }

});

proxyHost.on("upgrade", (req: any, socket: any, head: any) => {
  const parsedHost = /^(\d+)-.*$/.exec(req.headers.host)
  if (parsedHost && parsedHost[1]) {
    const port = Number(parsedHost[1]);
    console.log(port)
    return proxy.ws(req, socket, head, {
        target: `http://localhost:${port}${req.url}`,
        ignorePath: true,
    });
  }
});

proxyHost.on("error", function (e) {
  console.log(e);
});

proxyHost.listen(Number(process.env.PORT) || 63901, "0.0.0.0");
