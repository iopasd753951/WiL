# 패키지 : 도트(.)를 이용하여 파이썬 모듈을 계층적으로 관리할 수 있게 해주는 것.

# 첫 번째 방법( python shall에서 실행 )


# echo.py
def echo_test():
    print ("echo")

    # C:/doit/game/sound에 있는 모듈을 만들어줌.


#render.py
def render_test():
    print("render")

    # C:/doit/game/graphic에 있는 모듈을 만들어줌.

# 이 때 각 파일마다 __init__.py라는 파일을 만든다.


# 패키지 안의 함수 실행하기

# 1번째

import game.sound.echo
game.sound.echo.echo_test()

--> echo 출력

# 2번째

from game.sound.echo import echo_test
echo.echo_test



#3번째
from game.sound.echo import echo_test
echo_test()

# 하지만 3번째 방법은 실행 불가하다.
# 왜냐하면 import game를 수행하면 디렉터리의 모듈 또는 game 디렉터리의 __init__.py에 정의된것들만 참조할 수 있기 때문이다.

# 도트연산자(.)를 사용하여 import할 때는 마지막 항목이 꼭 모듈 또는 패키지 여야만 한다..


__init__

# __init__.py이란 해당 디렉터리가 패키지의 일부임을 알려주는 역할을 해준다.


__all__

# __all__이란 패키지에서 import를 할 때에는 *사용이 되지 않기 때문에 __init__.py 파일에
# __all__이라는 변수를설정해주고 모듈을 정의 해주면 사용할 수 있다.

# C:/doit/game/sound/__init__.py   --->>    __all__ = ['echo']라고 적어준다.

# --init__.py에 적어주었다면 이제는 *을 쓸 수 있을 것이다.

from game.sound import *
echo.echo_test()



# graphic 디렉터리의 render.py 모듈이
# sound 디렉터리의 echo.py 모듈을 사용하고 싶을 때 render.py를 아래와 같이 수정하면된다.

# render.py
from game.sound.echo import echo_test
def render_test():
    print("render")
    echo_test()

# from game.sound.echo import echo_test라는 문장을 추가하여
# echo_test() 함수를 사용할 수 있도록 수정했다.


from game.graphic.render import render_test
render_test()






