# Django Jsend Responses


**Jsend specified Responses for APIs.**

---

# Overview

Django Jsend Responses supply response classes to use in projects created with Django.
See http://labs.omniti.com/labs/jsend for jsend spec.

----

# Requirements

* Django (1.11, 2.0, 2.1)

# Installation

Install using `pip`...

    pip install djangojsendresponses


# Examples

Success response:

    {
        "status": "success",
        "data": {
            "object": { 
                "id": 1, 
                "name": "Fist object"
            }
        }
    }
    

Fail response:

    {
        "status" : "fail",
        "data" : {
            "name" : "A name is required" 
        }
    }


Error response:

    {
        "status" : "error",
        "message" : "A service is unavailable to connect"
    }
