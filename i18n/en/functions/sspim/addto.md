# SSP messenger: Adding a recipient

Specifying a recipient by IP address and port number is cumbersome and often leads to mistakes.<br>
If you or the other person exchange messages over a dial-up Internet connection, the IP address may change for both of you each time you connect, making configuration difficult.

A directory service can help with this.

By specifying a user ID (email address), you can look up people logged in to the same directory service by name alone. In SSP, 「SSP and Friends」 is the default server, which anyone can use freely without a password.<br>
※In exchange for making your own information public, you can retrieve the other person's information. Therefore, even if you have a fixed IP address, you need to log in to a directory service to find someone with a changing IP address.<br>
※The only information that can be shared and retrieved is the IP address and the port number used to wait for incoming SSTP connections.

You can also save a name and IP address combination locally, though this is probably less common. This works as long as both parties have fixed IP addresses, whether on the Internet or a local network. It also lets you send messages immediately by skipping the lookup.

## Registering a directory service user

In the dialog that appears when you select 「Add recipient」 from 「Register」, first select 「Directory service」.

Next, enter the other person's name and group. These are used to identify the information registered in SSP.

Select the directory service that the other person is logged in to. You can register directory services in the [Preferences dialog](../../config/im.md).

The user ID is usually the other person's email address. However, it must be the user ID they use to log in, so ask them which one to use.

This completes the registration. When you send a message, SSP will automatically retrieve the other person's address and send it.

## Registering a user by specifying an IP address directly

In the dialog that appears when you select 「Add recipient」 from 「Register」, select 「Specify address」.

Next, enter the other person's name and group. These are used to identify the information registered in SSP.

Enter the other person's IP address and the port number they use for SSP messenger.

This completes the registration.
