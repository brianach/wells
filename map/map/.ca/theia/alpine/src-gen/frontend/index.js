// @ts-check
require('es6-promise/auto');
require('reflect-metadata');
require('setimmediate');
const { Container } = require('inversify');
const { FrontendApplicationConfigProvider } = require('@theia/core/lib/browser/frontend-application-config-provider');

FrontendApplicationConfigProvider.set({
    "applicationName": "Codeanywhere",
    "defaultTheme": "Codeanywhere Dark",
    "defaultIconTheme": "theia-file-icons",
    "electron": {
        "windowOptions": {}
    },
    "defaultLocale": "",
    "validatePreferencesSchema": true,
    "preferences": {
        "files.enableTrash": false,
        "ruby.useLanguageServer": true,
        "php.suggest.basic": false,
        "python.jediEnabled": false,
        "http.proxySupport": "off"
    },
    "warnOnPotentiallyInsecureHostPattern": false
});


self.MonacoEnvironment = {
    getWorkerUrl: function (moduleId, label) {
        return './editor.worker.js';
    }
}

const preloader = require('@theia/core/lib/browser/preloader');

// We need to fetch some data from the backend before the frontend starts (nls, os)
module.exports = preloader.preload().then(() => {
    const { FrontendApplication } = require('@theia/core/lib/browser');
    const { frontendApplicationModule } = require('@theia/core/lib/browser/frontend-application-module');
    const { messagingFrontendModule } = require('@theia/core/lib/browser/messaging/messaging-frontend-module');
    const { loggerFrontendModule } = require('@theia/core/lib/browser/logger-frontend-module');

    const container = new Container();
    container.load(frontendApplicationModule);
    container.load(messagingFrontendModule);
    container.load(loggerFrontendModule);

    return Promise.resolve()
    .then(function () { return Promise.resolve(require('@theia/core/lib/browser/i18n/i18n-frontend-module')).then(load) })
    .then(function () { return Promise.resolve(require('@theia/core/lib/browser/menu/browser-menu-module')).then(load) })
    .then(function () { return Promise.resolve(require('@theia/core/lib/browser/window/browser-window-module')).then(load) })
    .then(function () { return Promise.resolve(require('@theia/core/lib/browser/keyboard/browser-keyboard-module')).then(load) })
    .then(function () { return Promise.resolve(require('@theia/core/lib/browser/request/browser-request-module')).then(load) })
    .then(function () { return Promise.resolve(require('@codeanywhere/theia-ca-about-us/lib/browser/frontend-module')).then(load) })
    .then(function () { return Promise.resolve(require('@codeanywhere/theia-ports/lib/browser/frontend-module')).then(load) })
    .then(function () { return Promise.resolve(require('@theia/filesystem/lib/browser/filesystem-frontend-module')).then(load) })
    .then(function () { return Promise.resolve(require('@theia/filesystem/lib/browser/download/file-download-frontend-module')).then(load) })
    .then(function () { return Promise.resolve(require('@theia/filesystem/lib/browser/file-dialog/file-dialog-module')).then(load) })
    .then(function () { return Promise.resolve(require('@theia/variable-resolver/lib/browser/variable-resolver-frontend-module')).then(load) })
    .then(function () { return Promise.resolve(require('@theia/editor/lib/browser/editor-frontend-module')).then(load) })
    .then(function () { return Promise.resolve(require('@theia/process/lib/common/process-common-module')).then(load) })
    .then(function () { return Promise.resolve(require('@theia/workspace/lib/browser/workspace-frontend-module')).then(load) })
    .then(function () { return Promise.resolve(require('@theia/terminal/lib/browser/terminal-frontend-module')).then(load) })
    .then(function () { return Promise.resolve(require('@codeanywhere/theia-shareit/lib/browser/frontend-module')).then(load) })
    .then(function () { return Promise.resolve(require('@codeanywhere/theia-workspace-keep-alive/lib/browser/frontend-module')).then(load) })
    .then(function () { return Promise.resolve(require('@codeanywhere/theia-ca-base-config/lib/browser/frontend-module')).then(load) })
    .then(function () { return Promise.resolve(require('@codeanywhere/theia-ca-branding/lib/browser/frontend-module')).then(load) })
    .then(function () { return Promise.resolve(require('@theia/mini-browser/lib/browser/mini-browser-frontend-module')).then(load) })
    .then(function () { return Promise.resolve(require('@theia/mini-browser/lib/browser/environment/mini-browser-environment-module')).then(load) })
    .then(function () { return Promise.resolve(require('@codeanywhere/theia-ca-mini-browser/lib/browser/frontend-module')).then(load) })
    .then(function () { return Promise.resolve(require('@theia/markers/lib/browser/problem/problem-frontend-module')).then(load) })
    .then(function () { return Promise.resolve(require('@theia/outline-view/lib/browser/outline-view-frontend-module')).then(load) })
    .then(function () { return Promise.resolve(require('@theia/monaco/lib/browser/monaco-frontend-module')).then(load) })
    .then(function () { return Promise.resolve(require('@theia/userstorage/lib/browser/user-storage-frontend-module')).then(load) })
    .then(function () { return Promise.resolve(require('@theia/preferences/lib/browser/preference-frontend-module')).then(load) })
    .then(function () { return Promise.resolve(require('@codeanywhere/theia-code-runner-config/lib/browser/frontend-module')).then(load) })
    .then(function () { return Promise.resolve(require('@theia/navigator/lib/browser/navigator-frontend-module')).then(load) })
    .then(function () { return Promise.resolve(require('@theia/preview/lib/browser/preview-frontend-module')).then(load) })
    .then(function () { return Promise.resolve(require('@codeanywhere/theia-init-file-open/lib/browser/frontend-module')).then(load) })
    .then(function () { return Promise.resolve(require('@codeanywhere/theia-remove-workspace-menus/lib/browser/frontend-module')).then(load) })
    .then(function () { return Promise.resolve(require('@codeanywhere/theia-workspace-id-from-url-getter/lib/browser/frontend-module')).then(load) })
    .then(function () { return Promise.resolve(require('@theia/bulk-edit/lib/browser/bulk-edit-frontend-module')).then(load) })
    .then(function () { return Promise.resolve(require('@theia/callhierarchy/lib/browser/callhierarchy-frontend-module')).then(load) })
    .then(function () { return Promise.resolve(require('@theia/console/lib/browser/console-frontend-module')).then(load) })
    .then(function () { return Promise.resolve(require('@theia/output/lib/browser/output-frontend-module')).then(load) })
    .then(function () { return Promise.resolve(require('@theia/task/lib/browser/task-frontend-module')).then(load) })
    .then(function () { return Promise.resolve(require('@theia/debug/lib/browser/debug-frontend-module')).then(load) })
    .then(function () { return Promise.resolve(require('@theia/editor-preview/lib/browser/editor-preview-frontend-module')).then(load) })
    .then(function () { return Promise.resolve(require('@theia/file-search/lib/browser/file-search-frontend-module')).then(load) })
    .then(function () { return Promise.resolve(require('@theia/keymaps/lib/browser/keymaps-frontend-module')).then(load) })
    .then(function () { return Promise.resolve(require('@theia/getting-started/lib/browser/getting-started-frontend-module')).then(load) })
    .then(function () { return Promise.resolve(require('@theia/scm/lib/browser/scm-frontend-module')).then(load) })
    .then(function () { return Promise.resolve(require('@theia/scm-extra/lib/browser/scm-extra-frontend-module')).then(load) })
    .then(function () { return Promise.resolve(require('@theia/git/lib/browser/git-frontend-module')).then(load) })
    .then(function () { return Promise.resolve(require('@theia/git/lib/browser/prompt/git-prompt-module')).then(load) })
    .then(function () { return Promise.resolve(require('@theia/memory-inspector/lib/browser/memory-inspector-frontend-module')).then(load) })
    .then(function () { return Promise.resolve(require('@theia/messages/lib/browser/messages-frontend-module')).then(load) })
    .then(function () { return Promise.resolve(require('@theia/search-in-workspace/lib/browser/search-in-workspace-frontend-module')).then(load) })
    .then(function () { return Promise.resolve(require('@theia/timeline/lib/browser/timeline-frontend-module')).then(load) })
    .then(function () { return Promise.resolve(require('@theia/typehierarchy/lib/browser/typehierarchy-frontend-module')).then(load) })
    .then(function () { return Promise.resolve(require('@theia/plugin-ext/lib/plugin-ext-frontend-module')).then(load) })
    .then(function () { return Promise.resolve(require('@theia/plugin-dev/lib/browser/plugin-dev-frontend-module')).then(load) })
    .then(function () { return Promise.resolve(require('@theia/plugin-ext-vscode/lib/browser/plugin-vscode-frontend-module')).then(load) })
    .then(function () { return Promise.resolve(require('@theia/plugin-metrics/lib/browser/plugin-metrics-frontend-module')).then(load) })
    .then(function () { return Promise.resolve(require('@theia/property-view/lib/browser/property-view-frontend-module')).then(load) })
    .then(function () { return Promise.resolve(require('@theia/toolbar/lib/browser/toolbar-frontend-module')).then(load) })
    .then(function () { return Promise.resolve(require('@theia/vsx-registry/lib/browser/vsx-registry-frontend-module')).then(load) })
        .then(start).catch(reason => {
            console.error('Failed to start the frontend application.');
            if (reason) {
                console.error(reason);
            }
        });

    function load(jsModule) {
        return Promise.resolve(jsModule.default)
            .then(containerModule => container.load(containerModule));
    }

    function start() {
        (window['theia'] = window['theia'] || {}).container = container;
        return container.get(FrontendApplication).start();
    }
});
