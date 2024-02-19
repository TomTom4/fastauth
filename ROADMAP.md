# Free Auth
This project is an attempt to implement the [Oauth2 standard](https://datatracker.ietf.org/doc/html/rfc6749),
and its [Bearer Token specification](https://datatracker.ietf.org/doc/html/rfc6750).
It aim to provide a simple solution to those who might be interested into a free self 
hosted auth server.

> If you are looking fore a production ready open source  project that provide all the
features cited below, then consider visiting [superToken]("https://supertokens.com/").

## AuthServer

### first milestone: Access Token provider

By the end of this milestone, we should have a basic username and password authentication
server.
it should provide:

 - [ ] a register endpoint to register with a username and password
 - [ ] a signin endpoint to get the access token.
 - [ ] a delete account endpoint for account deletion. 