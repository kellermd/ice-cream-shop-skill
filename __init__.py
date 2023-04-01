from mycroft import MycroftSkill, intent_file_handler


class IceCreamShop(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('shop.cream.ice.intent')
    def handle_shop_cream_ice(self, message):
        flavor = message.data.get('flavor')

        self.speak_dialog('shop.cream.ice', data={
            'flavor': flavor
        })


def create_skill():
    return IceCreamShop()

