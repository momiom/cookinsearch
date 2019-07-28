from linebot.models import (BubbleContainer, ImageComponent, BoxComponent,
                            TextComponent, SpacerComponent, IconComponent,
                            ButtonComponent, SeparatorComponent, URIAction,
                            CarouselContainer)
import logging


class CarouselCreator:
    @staticmethod
    def create_carousel(items):
        # Flaskのロガーを取得
        logger = logging.getLogger('flask.app')
        logger.debug(len(items))

        bubbles = []
        for item in items[:10]:
            hero = ImageComponent(
                url=item.img,
                size='full',
                aspect_ratio='20:13',
                aspect_mode='cover',
                action=URIAction(uri=item.url, label='label')
            )
            
            # body
            title_text_component = TextComponent(
                        text=item.title,
                        weight='bold',
                        size='lg',
                        color='#5c5752'
                    )
            # tagをTextComponentの配列に
            tag_components = []
            for tag in item.tags:
                tag_components.append(TextComponent(
                    text=tag,
                    size='sm',
                    color='#5c5752'
                ))
            # 組み立て
            body = BoxComponent(
                layout='vertical',
                contents=[
                    # title
                    title_text_component,
                    # tags
                    BoxComponent(
                        layout='baseline',
                        margin='md',
                        contents=tag_components
                    ),
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
                                        flex=1
                                    ), 
                                    TextComponent(
                                        text='Shinjuku, Tokyo',
                                        wrap=True,
                                        color='#666666',
                                        size='sm',
                                        flex=5
                                    )
                                ], 
                            ),
                            BoxComponent(
                                layout='baseline',
                                spacing='sm',
                                contents=[
                                    TextComponent(
                                        text='Time',
                                        color='#aaaaaa',
                                        size='sm',
                                        flex=1
                                    ),
                                    TextComponent(
                                        text="10:00 - 23:00",
                                        wrap=True,
                                        color='#666666',
                                        size='sm',
                                        flex=5,
                                    ),
                                ], 
                            ),
                        ], 
                    )
                ], 
            )
            footer = BoxComponent(
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
                ]
            )

            bubble = BubbleContainer(
                direction='ltr',
                hero=hero,
                body=body,
                footer=footer, 
            )
            bubbles.append(bubble)
        
        carousel = CarouselContainer(bubbles)
        return carousel


if __name__ == "__main__":
    carousel_template = CarouselCreator.create_carousel([])
    print(carousel_template)
