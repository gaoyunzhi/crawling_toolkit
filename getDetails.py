try:
    from BeautifulSoup import BeautifulSoup,SoupStrainer
except:
    from bs4 import BeautifulSoup,SoupStrainer # beta version of bs
from getWebpage import getWebpage

def clean(s):
    ans=[]
    for i in s:
        if ord(i)<128:
            ans.append(i)
        else:
            ans.append(' ')
    return (''.join(ans)).strip()

def removeNonAscii(s):
    ans=[]
    for i in s:
        if ord(i)<128:
            ans.append(i)
        else:
            ans.append(' ')
    return ''.join(ans)

def getDetails(page):
    detail={}
    page=str(page)
    soup=BeautifulSoup(page)
    productSize=soup.find('dd',{'class':'productSize'})
    try:
        SizeContent=productSize.contents
    except:
        return {}
    size=SizeContent[0].strip()
    pricePersize=SizeContent[-1].strip()
    for line in SizeContent[1:]:
        try:
            line=line.strip()
            if line[0]=='$':
                pricePersize=line
        except:
            continue
    price=soup.find('dd',{'class':'productPrice'})
    price=price.contents[0].strip()
    detail['size']=size
    detail['pricePerSize']=pricePersize
    detail['price']=price
    
    nutrition=soup.find('div',{'class':'productDetailsContent'})
    #print nutrition
    tds=[]
    for node in nutrition.findAll('td'):
        tds.append(''.join(node.findAll(text=True)))
    tds_new=[]
    for td in tds:
        try:
            td=td.encode("ascii","replace")
            td=str(td)
            td=td.strip()
            td=td.replace('?',' ')
            td=td.strip()
            tds_new.append(td)
        except:
            continue
    tds=tds_new
    for td in tds:
        if td.startswith('Serving Size'):
            servingSize=td[len('Serving Size')+1:].strip()
        if td.startswith('Servings Per Container'):
            servingsPerContainer=td[len('Servings Per Container')+1:].strip()
        if len(td)>0 and td[-1] in map(str,range(10))+['%','g']:
            index1=td.rfind('?')
            index2=td.rfind(' ')
            index=max(index1, index2)
            if index==-1: continue
            name=td[:index].strip()
            value=td[index+1:].strip()
            if len(value)>20 or len(name)>40: continue
            if not name in detail: detail[name]=value
    
    
    try:
        detail['servingSize']=servingSize
    except:
        pass
    try:
        detail['servingsPerContainer']=servingsPerContainer
    except:
        pass
    
    #print nutrition
    try:
        ingredients=nutrition.findAll('div')[-1]
        detail['ingredients']=ingredients.contents[-1].strip()
    except:
        pass

    try:
        second=soup.findAll('div',{'class':'productDetailsContent'})[-1]
        if not str(second.contents[3]).startswith('<'):
            detail['info']=clean(str(second.contents[2])+str(second.contents[3]))
            startInd=4
        else:
            detail['info']=clean(str(second.contents[2]))
            startInd=3
        for info in str(second.contents[startInd]).split('<b>'):
            info=removeNonAscii(info)
            info=str(info)
            info=info.strip()
            info=info.replace('?',' ')
            info=info.strip()
            index=info.find('<br>')
            info=info[:index]
            index=info.find('</b>')
            info_name=info[:index].strip()
            if info_name[-1]==':': info_name=info_name[:-1]
            info_value=info[index+4:].strip()
            if not info_name in detail: detail[info_name]=info_value
    except:
        pass
     
    new_detail={}
    for x in detail:
        if '\n' in x: continue
        name=x
        if name=='Servings Per Container about': name='servingsPerContainer'
        if name=='servingsPerContainer': name='Servings Per Container'
        if name=='servingSize': name='Serving Size'
        value=detail[x]
        if name[-1]==':': name=name[:-1]
        if len(name)<3: continue
        new_detail[name]=value
    for x in detail:
        name=x
        value=detail[x]
        if len(name.split())>1 and name[-1] in map(str,range(10))+['%','g']:
            value=clean(name.split()[-1])
            name=clean(' '.join(name.split()[:-1]))
            tmpname=None
            if name.endswith('Calories from Fat'):
                tmpname=name
                name='Calories from Fat'
            if not name in new_detail:
                new_detail[name]=value
            if tmpname!=None:
                tmpname=tmpname.split()
                if tmpname[0]=='Calories' and len(tmpname)>1:
                    value=tmpname[1]
                    new_detail['Calories']=value
    return new_detail


        
page=getWebpage('http://www.peapod.com/itemDetailView.jhtml?productId=155508',dataDir='../../data/detail_pages')

getDetails(page)
