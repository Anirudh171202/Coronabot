## happy path
* greet
  - utter_greet
  - utter_functions
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
  - utter_functions
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
  - utter_functions
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## helpline path
* greet
  - utter_greet
  - utter_functions
* fetch_country{"country":"Country"}
  - action_fetchcases
* fetch_helpline
  - utter_helpline
* coronavirusaffectedmajor
  - utter_coronavirusaffectedmajor

* coronavirusmortaliltywhat
  - utter_coronavirusmortaliltywhat

* COVID19likelycatch
  - utter_COVID19likelycatch

* developingillnessrisk
  - utter_developingillnessrisk

* protectshouldmyself
  - utter_protectshouldmyself

* COVID19catchfrom
  - utter_COVID19catchfrom

* surviveviruslong
  - utter_surviveviruslong

* contractsymptomsshould
  - utter_contractsymptomsshould

* precautionsqaurantinetaken
  - utter_precautionsqaurantinetaken

* protectshouldmyself
  - utter_protectshouldmyself

* coronaknowhave
  - utter_coronaknowhave

* hydroxychloroquinecoronaviruscure
  - utter_hydroxychloroquinecoronaviruscure

* coronavirusspreaddoes
  - utter_coronavirusspreaddoes

* outsidesafeis
  - utter_outsidesafeis

* coronavirushumansspread
  - utter_coronavirushumansspread

* COVID19Shouldtested
  - utter_COVID19Shouldtested

* COVID19testedwhere
  - utter_COVID19testedwhere

* communityoutbreakshould
  - utter_communityoutbreakshould

* cleaningproductsCOVID19
  - utter_cleaningproductsCOVID19

* differentsymptomsCOVID19
  - utter_differentsymptomsCOVID19

* COVID19contactsomeone
  - utter_COVID19contactsomeone

* patientsdonateblood
  - utter_patientsdonateblood

* internationalpackagesrecieve
  - utter_internationalpackagesrecieve

* COVID19seeingcases
  - utter_COVID19seeingcases

* conditionsCOVID19what
  - utter_conditionsCOVID19what


* goodbye
  - utter_goodbye


