SEMICOLON.Core.getVars.fn.bootstrap=o=>{var t=SEMICOLON.Core;t.loadJS({file:"plugins.bootstrap.js",id:"canvas-bootstrap-js",jsFolder:!0}),t.isFuncTrue(()=>"undefined"!=typeof bootstrap).then(o=>{if(!o)return!1;SEMICOLON.Core.initFunction({class:"has-plugin-bootstrap",event:"pluginBootstrapReady"})})};