# Usage

Even if the code isn't clean, and will need some more love and care, we can
already set up a basic use case example, that will serve both as a live solution to try on the achieved features, and as a usage example as well. 

Nowadays every existing backend framework implements its own authentication and (sometimes) its authorization services. Most of the time, it is more than enough. The only usecase where this get tricky and painfull is when you want to share your authentication and authorization solution across multiples services.

So this project is only usefull in a micro-service architecture environment.
We should then provide a basic micro-service architecture for our use case. 

Here is what we need:

1. this little auth server up and running
2. a client frontend that needs to do a couple of thing:
    - access public service
    - authentify
    - access protected service
3. we need a service for our client to connect to, that would verify our client token using our authentication service
