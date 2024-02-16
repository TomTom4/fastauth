# Free Auth
> This is an exploratory project to help me understand AUth server and 
[Oauth2 standard](https://datatracker.ietf.org/doc/html/rfc6749) and deeper 
understanding on what is going on within Authentication and Authorization servers.
If you are looking fore a production ready open source  project that provide all the
features cited below, then consider visiting [superToken]("https://supertokens.com/").
However, if you are like me not satisfied with the main existing solutions, and are 
looking for something else, you are in the right place!

Aim to provide a fully Oauth2 compliant authentication server.
the chosen stack will be fastAPI in combination with MongoDB.

## AuthServer


features:
- as an Admin I want to be able to set up roles
- as an Admin I want to be able to register a User with its email without knowing its
  password
- as an Admin I want to be able to set a User role in order to give access to some part
  my service.
- as an Admin I want to be able to remove a User role in order to restrict access to 
  service.
- as an Admin I want to be able to force signout of a User.
- as an Admin I want to be able to delete a User.
- as a User I want to be able to register with an email and a password 
  in order to use the service
- as a User I want to be able to signin in order to use the protected service
- as a User I want a convenient solution to confirm my email in order to show that it
  is usable as a communication medium
- as a User I want to be able to change my password if I forgot it.
- as a User I want to be able to signout in order to protect my account.
- as a User I want to be able to delete my account in order to protect my email.


## management cli
A management cli should be provided to do all the Admin actions. In adition, it should
provide owner to set up Admin account, and the ability to activate or deactivate the 
Admin API.
