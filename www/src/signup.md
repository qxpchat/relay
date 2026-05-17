# Sign up

`{{ config.mail_domain }}` runs the chatmail relay that powers `@{{ config.mail_domain }}` addresses. New qxp accounts get a random `@{{ config.mail_domain }}` address — no signup form, no phone number, no personal data collected. You can switch to any other chatmail relay at any time without losing your contacts.

<div class="qr-section">
  <a id="qr-link" href="#" class="qr-wrap">
    <div id="qr-code"></div>
    <img class="qr-logo" src="/logo.svg" alt="" />
  </a>

  <a class="cta-button" id="dclogin-link" href="#">Get a {{config.mail_domain}} chat profile</a>

  <ol class="steps">
    <li><span class="step-num">1.</span><span>🐣 <strong>Choose</strong> your avatar and name</span></li>
    <li><span class="step-num">2.</span><span>💬 <strong>Start</strong> chatting using QR invite codes</span></li>
  </ol>
</div>

<script src="/qrcode-svg.min.js"></script>
<script src="/dclogin.js"></script>

---

## More information

`{{ config.mail_domain }}` provides a low-maintenance, resource-efficient and interoperable email service for everyone. A chatmail address is effectively a normal email address, just optimized for use in chats — especially with [qxp](https://qxp.chat) and other [chatmail clients](https://chatmail.at/clients).

### Rate and storage limits

- Unencrypted messages are blocked to recipients outside `{{ config.mail_domain }}`. Setting up contact via [QR invite codes](https://chatmail.at) lets your messages pass freely to any outside recipient.
- You may send up to {{ config.max_user_send_per_minute }} messages per minute.
- You can store up to {{ config.max_mailbox_size }} of messages on the server.
- Messages are unconditionally removed after {{ config.delete_mails_after }} days. Earlier if storage would otherwise be exceeded.

### <a name="account-deletion"></a> Account deletion

If you remove a `{{ config.mail_domain }}` profile from within the qxp app, the account on the server (along with all associated data) is automatically deleted {{ config.delete_inactive_users_after }} days afterwards.

If you use multiple devices, remove the profile from each device for all account data to be deleted server-side.

### Who runs this?

This relay is operated by the qxp project. The chatmail server software is open source — you can find our fork at [github.com/qxpchat/relay](https://github.com/qxpchat/relay). Upstream lives at [github.com/chatmail/relay](https://github.com/chatmail/relay).
