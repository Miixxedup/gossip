# gossip
A bookalike register with gossip from everyone!

# strapi datamodel

Not automated, so here is what to do in words:
- Plugins -> Content-Types Builder
- + Create new collection type
- Name it Gossip
- Add a field -> text
- Base Settings -> Name : 'indicator', Type : Short text
- Advanced Settings -> Check Required, Check Unique
- Add a field -> text
- Base Settings -> Name : 'comment', Type : Long text
- Advanced Settings -> Check Required
- add a field -> enum
- Base Settings -> Name : 'type', Values : API \n USER \n CORRELATION
- Advanced Settings -> Check Required
- Save
- Settings -> Users -> Roles -> Public -> Permissions -> GOSSIP -> Check find
- Save
- Collection Types -> Gossips -> Add new Gossips
- Add a Gossip
- Try finding it with gossip.py -s {indicator} 

