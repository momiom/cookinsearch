from linebot.models import (BubbleContainer, ImageComponent, BoxComponent,
                            TextComponent, SpacerComponent, IconComponent,
                            ButtonComponent, SeparatorComponent, URIAction)


class CarouselCreator:
    @staticmethod
    def create_carousel(items):
        bubble = BubbleContainer(
            direction='ltr',
            hero=ImageComponent(
                url='https://example.com/cafe.jpg',
                size='full',
                aspect_ratio='20:13',
                aspect_mode='cover',
                action=URIAction(uri='http://example.com', label='label')),
            body=BoxComponent(
                layout='vertical',
                contents=[
                    # title
                    TextComponent(text='Brown Cafe', weight='bold', size='xl'),
                    # review
                    BoxComponent(
                        layout='baseline',
                        margin='md',
                        contents=[
                            IconComponent(
                                size='sm',
                                url='https://example.com/gold_star.png'),
                            IconComponent(
                                size='sm',
                                url='https://example.com/grey_star.png'),
                            IconComponent(
                                size='sm',
                                url='https://example.com/gold_star.png'),
                            IconComponent(
                                size='sm',
                                url='https://example.com/gold_star.png'),
                            IconComponent(
                                size='sm',
                                url='https://example.com/grey_star.png'),
                            TextComponent(
                                text='4.0',
                                size='sm',
                                color='#999999',
                                margin='md',
                                flex=0)
                        ]),
                    # info
                    BoxComponent(
                        layout='vertical',
                        margin='lg',
                        spacing='sm',
                        contents=[
                            BoxComponent(
                                layout='baseline',
                                spacing='sm',
                                contents=[
                                    TextComponent(
                                        text='Place',
                                        color='#aaaaaa',
                                        size='sm',
                                        flex=1), TextComponent(
                                            text='Shinjuku, Tokyo',
                                            wrap=True,
                                            color='#666666',
                                            size='sm',
                                            flex=5)
                                ], ),
                            BoxComponent(
                                layout='baseline',
                                spacing='sm',
                                contents=[
                                    TextComponent(
                                        text='Time',
                                        color='#aaaaaa',
                                        size='sm',
                                        flex=1),
                                    TextComponent(
                                        text="10:00 - 23:00",
                                        wrap=True,
                                        color='#666666',
                                        size='sm',
                                        flex=5, ),
                                ], ),
                        ], )
                ], ),
            footer=BoxComponent(
                layout='vertical',
                spacing='sm',
                contents=[
                    # callAction, separator, websiteAction
                    SpacerComponent(size='sm'),
                    # callAction
                    ButtonComponent(
                        style='link',
                        height='sm',
                        action=URIAction(label='CALL', uri='tel:000000'), ),
                    # separator
                    SeparatorComponent(),
                    # websiteAction
                    ButtonComponent(
                        style='link',
                        height='sm',
                        action=URIAction(
                            label='WEBSITE', uri="https://example.com"))
                ]), )
        return bubble

if __name__ == "__main__":
    carousel_template = CarouselCreator.create_carousel([])
    print(carousel_template)