## 02. 고급 HTML 분석

#### HTML 페이지를 조각조각 분석해봅시다. 일단 시작하기 전에..    

HTML페이지가 생각보다 훨씬 못생겼을 수 있습니다. 그렇다면,
```
- 좀 더 나은 html 구조를 갖춘 같은 문서가 있을 지 찾아보세요(인쇄용 페이지라거나, 모바일 버전 사이트라거나..)
- 필요한 정보가 html이 아니라 javascript 파일 안에 숨어있을 지도 모릅니다.
- 가끔은 원하는 정보가 페이지 내용이 아니라 URL에 들어있을 지도 몰라요.
- 이 사이트가 너무나 더럽다면, 혹시 같은 정보를 조금 더 나은 다른 사이트에서 구할 수는 없을 지 찾아보세요.
```    


이 장에서는 다시 BeautifulSoup를 사용합니다.
하지만 다른 대안들도 있으니 경우에 따라 다른 라이브러리를 사용하는 것도 고려해보세요.
- [lxml](https://www.google.co.kr/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0ahUKEwji1qDd0cvUAhWKwbwKHTwYBuYQFggrMAA&url=http%3A%2F%2Flxml.de%2F&usg=AFQjCNF-QT8NZg_5cU6_TALZYuOp8BWGug&sig2=JPoeew1UqHWZ0689eUvNnA)
- [HTML 파서](https://docs.python.org/3/library/html.parser.html)

#### BeautifulSoup를 사용해서 HTML 분석하기    

##### attribute를 사용해서 html 태그 검색하기 : 이름과 속성에 따라 찾기
  - find()
  - findAll()

##### 트리를 이동해가며 태그 검색하기 : 위치에 따라 찾기
  - 자식children과 자손decendents
  - 형제sibling
  - 부모parent   
