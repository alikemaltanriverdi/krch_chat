export default function(u){const g=SEMICOLON.Core;g.loadJS({file:"plugins.cookie.js",id:"canvas-cookie-js",jsFolder:!0}),g.isFuncTrue(()=>"undefined"!=typeof Cookies).then(e=>{if(!e)return!1;if(g.initFunction({class:"has-plugin-cookie",event:"pluginCookieReady"}),(u=g.getSelector(u,!1)).length<1)return!0;let t=document.querySelector(".gdpr-settings"),o=(t?.getAttribute("data-speed"),t?.getAttribute("data-expire")||30),i=t?.getAttribute("data-delay")||1500,s=t?.getAttribute("data-persistent"),r="bottom",n=t?.offsetHeight+100,c=t?.offsetWidth+100,a,d=document.querySelector(".gdpr-cookie-settings"),l=d?.querySelectorAll("[data-cookie-name]");if(!t&&!d)return!0;t&&("true"==s&&Cookies.set("websiteUsesCookies",""),t?.classList.contains("gdpr-settings-sm")&&t?.classList.contains("gdpr-settings-right")?r="right":t?.classList.contains("gdpr-settings-sm")&&(r="left"),"left"==r?(a=-c,t.style.right="auto",t.style.marginLeft="1rem"):"right"==r?(a=-c,t.style.left="auto",t.style.marginRight="1rem"):a=-n,t.style[r]=a+"px","yesConfirmed"!=Cookies.get("websiteUsesCookies")&&setTimeout(()=>{t.style[r]=0,t.style.opacity=1},Number(i)),document.querySelector(".gdpr-accept").onclick=e=>{e.preventDefault(),t.style[r]=a+"px",t.style.opacity=0,Cookies.set("websiteUsesCookies","yesConfirmed",{expires:Number(o)})}),l?.forEach(e=>{var t=e.getAttribute("data-cookie-name"),t=Cookies.get(t);e.checked=void 0!==t&&"1"==t}),document.querySelector(".gdpr-save-cookies")&&(document.querySelector(".gdpr-save-cookies").onclick=e=>{e.preventDefault(),l.forEach(e=>{var t=e.getAttribute("data-cookie-name");1==e.checked?Cookies.set(t,"1",{expires:Number(o)}):Cookies.remove(t,"")}),0<d.closest(".mfp-content").length&&$.magnificPopup.close(),setTimeout(()=>{window.location.reload()},500)}),document.querySelectorAll(".gdpr-container")?.forEach(t=>{var e=t.getAttribute("data-cookie-name"),o=t.getAttribute("data-cookie-content"),i=t.getAttribute("data-cookie-content-ajax"),e=Cookies.get(e);void 0!==e&&"1"==e?(t.classList.add("gdpr-content-active"),i?fetch(i).then(e=>e.text()).then(e=>{e=(new DOMParser).parseFromString(e,"text/html");t?.insertAdjacentHTML("beforeend",e.body.innerHTML)}).catch(e=>{console.log(e)}):o&&(t.innerHTML+=o),g.runContainerModules(t)):t.classList.add("gdpr-content-blocked")})})}