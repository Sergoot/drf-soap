# drf-soap

### REST API на DRF c использованием SOAP сервиса

![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)

#### Endpoints

* **GET: api/v1/methods**  
Пример ответа сервера:  
`{  
   "methods": [
        "createDeclaration",  
        "declUnitsByClientId",  
        "declInfoByClientId",  
        "listClientId",  
        "declShortInfoByClientId",  
        "getUnitQueue",  
        "listPrivilege",  
        "getPrivilegeListByMo",  
        "getPrivilegePriority",  
        "listGroupSpec",  
        "getDouInfo",  
        "dictionaryInfo",  
        "getDistrictList",  
        "getUnitList",  
        "getVacantPlaceInfo",  
        "getDataComplect"  
     ]  
} `

* **GET: api/v1/methods/<Название метода>**   
   Пример ответа сервера:  
  `{  
    "method": "listGroupSpec",  
    "parameters": {  
        "ocato": "string",  
        "kladr": "string"  
   }  
} `
* **POST: api/v1/methods**    
   Тело запроса:  
* ` {  
    "method": "listGroupSpec",  
    "ocato": "string1",  
    "kladr": "string2"  
} 
 `  
 Пример ответа сервера:    
 ` {  
     "method": "listGroupSpec",  
     "response": [  
     {  
            "Id": 3,  
            "Name": "Нет",  
            "Code": "No",  
            "Description": "Нет"  
     }  
    ]  
} `
