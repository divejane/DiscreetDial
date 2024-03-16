# DiscreetDial

Enigma, but in the terminal! Revolutionary. Doesn't get much better than this. There's really not a whole lot else to be excited for, people!

## TODO (security, efficiency, etc.) 

### Client/Server tramsmisssion protocol switch to HTTP
Currently running the client/server protocol on TCP just because that's what we have the P2P protocol running on. Eventually going to switch client/server to HTTP because we have just about everything there based on a query/recieve structure.

### Message order verification 
This one is simple; We're just going to tack on a (time sent) section on a message packet after it's sent from the sender's client. From there, the recieving client(s) can determine the order of the messages based off of who sent what first.

### Create the walls around our doorways
Right now, there's not a lot of error-checking on the server-side code. This makes our one (1) singular server prone to not only crashing, but potentially leaking senstivive information to some dork that wants to access it for whatever reason (federal agents). At some point, we'll secure any potentially sensitive data by error-checking a little harder, but also building a more strict framework that'll refuse interaction with any abnormal connections, avoiding a potential crash or data leak.  

## Minor changes:
- Change open-room-close requests to only be obeyed if the host of the room confirms itself as having connected to a peer
- Server only sends connection information to join-clients if that client explicitly requests the information of that room. Small change, and honestly won't change a whole lot, but at least somewhat avoids sending a massive list full of a connection information to a (potentially malicious) client
