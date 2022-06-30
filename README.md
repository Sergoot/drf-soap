# drf-soap

### REST API на DRF c использованием SOAP сервиса

#### Endpoints

* **GET: api/v1/methods**
  Пример ответа сервера:
  ` {
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
  ` {
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
