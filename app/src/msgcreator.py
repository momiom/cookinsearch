from linebot.models import (BubbleContainer, ImageComponent, BoxComponent,
                            TextComponent, SpacerComponent, IconComponent,
                            ButtonComponent, SeparatorComponent, URIAction,
                            CarouselContainer)
import logging
from const import *


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
                        color='#5c5752',
                    )
            # tagをTextComponentの配列に整形
            tag_components = []
            for i, tag in enumerate(item.tags):
                if i == 0:
                    tag_components.append(
                        TextComponent(
                            text=tag,
                            size='sm',
                            color='#5c5752',
                            flex=0,
                        )
                    )
                    continue
                tag_components.append(
                    TextComponent(
                        text=tag,
                        size='sm',
                        color='#5c5752',
                        flex=1,
                    )
                )
            # 調理方法をiconComponentとtextComponentの配列に整形
            cooking_method_components = []
            for method in item.cooking_methods:
                cooking_method_components.append(
                    IconComponent(
                        url=DOMAIN + method['icon'],
                        size='sm',
                        color='#5c5752'
                    )
                )
                cooking_method_components.append(
                    TextComponent(
                        text=method['name'],
                        size='sm',
                        color='#5c5752',
                        flex=1
                    )
               )
            # 組み立て
            body = BoxComponent(
                layout='vertical',
                contents=[
                    # title
                    title_text_component,
                    
                    # tags, cooking methods
                    BoxComponent(
                        layout='vertical',
                        margin='md',
                        spacing='xl',
                        contents=[
                            BoxComponent(
                                layout='baseline',
                                spacing='xl',
                                contents=tag_components
                            ),
                            BoxComponent(
                                layout='baseline',
                                spacing='sm',
                                contents=cooking_method_components
                            )
                        ]
                    ),
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
