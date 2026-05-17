<!-- invite.html — standalone invite-link landing page.
     Analog of deltachat/invite (i.delta.chat), built into the qxp
     static site. Styling reuses main.css (.qr-section, .steps,
     .qr-wrap, .cta-button); page-specific rules live in main.css
     under "Invite page". -->

<div id="say-hello" class="qr-section hidden">
  <h1><span id="join">Say hello to</span> <span class="invite-name" id="name">…</span> 👋</h1>
  <ol class="steps">
    <li><span class="step-num">1.</span><a class="cta-button" href="/">Download qxp</a></li>
    <li><span class="step-num">2.</span><a class="cta-button" id="dc-link" href="">Open chat</a></li>
  </ol>
  <details>
    <summary>I have qxp on another device</summary>
    <div id="qrcode" class="qr-wrap"></div>
    <p><em>Scan to open the chat on the other device.</em></p>
  </details>
</div>

<script src="/qrcode-svg.min.js"></script>
<script>
(function () {
    var searchParams = new URLSearchParams(window.location.hash.substr(1));
    var inputData = window.location.hash.substr(1);

    if (!inputData) {
        window.location.replace("/");
        return;
    }

    // convert `<FPR>&n=<NAME>...` to `OPENPGP4FPR:<FPR>#<NAME>...`
    var openpgp4fprStr = "OPENPGP4FPR:" + inputData.replace(/&/, "#");
    document.getElementById("dc-link").setAttribute("href", openpgp4fprStr);

    if (searchParams.get("g") || searchParams.get("b")) {
        document.getElementById("join").innerText = "Join";
    }
    document.getElementById("name").innerText =
        searchParams.get("g") || searchParams.get("b") ||
        searchParams.get("n") || searchParams.get("a") || "this contact";

    var qr = new QRCode({ content: openpgp4fprStr, width: 280, height: 280, padding: 0, join: true });
    document.getElementById("qrcode").innerHTML = qr.svg();

    document.getElementById("say-hello").classList.remove("hidden");
}());
</script>
