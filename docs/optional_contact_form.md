# Optional Contact Form

An optional contact form is possible but not included as it requires registration.

The following can be configured and added to the `contact-us` page as needed.

```html
    <!-- ============================================================ -->
    <!-- Contact Form                                                  -->
    <!-- Uses Formspree — free static form service, no server needed. -->
    <!--                                                               -->
    <!-- To activate:                                                  -->
    <!--   1. Go to https://formspree.io and sign up (free).          -->
    <!--   2. Create a new form — copy the form ID it gives you.      -->
    <!--   3. Replace YOUR_FORM_ID in the action URL below.           -->
    <!--   4. Formspree emails submissions to the address you choose.  -->
    <!--                                                               -->
    <!-- Until YOUR_FORM_ID is replaced, submissions are not sent.    -->
    <!-- ============================================================ -->
    <section id="contact-form">
      <h2>Contact Form</h2>
      <p>You can also use the form below. Submissions go to the district secretary
         and will be directed to the appropriate person.</p>

      <form action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
        <label for="contact-name">Name <span aria-hidden="true">*</span></label>
        <input type="text" id="contact-name" name="name" required autocomplete="name">

        <label for="contact-email">Email <span aria-hidden="true">*</span></label>
        <input type="email" id="contact-email" name="email" required autocomplete="email">

        <label for="contact-message">Message <span aria-hidden="true">*</span></label>
        <textarea id="contact-message" name="message" rows="6" required></textarea>

        <button type="submit">Send Message</button>
      </form>
```