import gossip_request
# Fill the strapi endpoint by faking args, most certainly the best way :)
print('Uploading some bogus data')
gossip_request.GossipRequest(['localhost', 'Lokaal mooi ontgonnen gebied, lachen maat', 'USER'], upload_test_data=True).store_request()
gossip_request.GossipRequest(['192.168.1.1', 'Lokaal mooi ontgonnen gebied, feestje hierzo', 'USER'], upload_test_data=True).store_request()
gossip_request.GossipRequest(['1.1.1.1', 'Lokaal mooi ontgonnen gebied, geintje toch', 'USER'], upload_test_data=True).store_request()
gossip_request.GossipRequest(['1.2.3.4', 'Lokaal mooi ontgonnen gebied, oplopend ook', 'USER'], upload_test_data=True).store_request()
gossip_request.GossipRequest(['4.4.4.4', 'Comment1', 'USER'], upload_test_data=True).store_request()
gossip_request.GossipRequest(['4.4.4.4', 'Comment2', 'USER'], upload_test_data=True).store_request()
gossip_request.GossipRequest(['4.4.4.4', 'Comment3', 'USER'], upload_test_data=True).store_request()
gossip_request.GossipRequest(['9.9.9.9', 'hier nog wat blablabla', 'USER'], upload_test_data=True).store_request()
gossip_request.GossipRequest(['172.2.0.1', 'Mooie test waardes', 'USER'], upload_test_data=True).store_request()
gossip_request.GossipRequest(['81.0.0.0.', 'Lokaal mooi ontgonnen gebied voor 81.0.0.0', 'USER'], upload_test_data=True).store_request()

