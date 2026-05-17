/* Profile generator: fetch random credentials from /new and render a
 * `dclogin:` QR code with the chatmail logo overlaid in the center.
 *
 * /new returns {email, password}. Upstream chatmail's newemail.py only
 * adds a pre-built dclogin_url when tls_cert_mode == "self"; for our
 * Let's Encrypt deploy it's absent, so we build the URL client-side.
 *
 * Requires qrcode-svg.min.js to be loaded first.
 */
(function () {
    function buildDcloginUrl(email, password) {
        // Mirror chatmaild/newemail.py:create_dclogin_url. Email is
        // already URL-safe (alphanumeric@domain); password may contain
        // punctuation and needs encoding.
        return 'dclogin:' + email + '?p=' + encodeURIComponent(password) + '&v=1';
    }

    function generateProfile() {
        fetch('/new', { method: 'POST' })
            .then(function (r) { return r.json(); })
            .then(function (data) {
                if (!data || !data.email || !data.password) {
                    throw new Error('malformed /new response');
                }
                var url = buildDcloginUrl(data.email, data.password);
                document.getElementById('dclogin-link').href = url;
                document.getElementById('qr-link').href = url;
                var qrCode = document.getElementById('qr-code');
                var qr = new QRCode({
                    content: url,
                    width: 280,
                    height: 280,
                    padding: 0,
                    join: true
                });
                qrCode.innerHTML = qr.svg();
            })
            .catch(function (err) {
                console.error('signup QR failed:', err);
            });
    }

    generateProfile();
})();
