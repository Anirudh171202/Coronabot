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
* mortaliltywhatrate
  - utter_mortaliltywhatrate
* likelycatchhow
  - utter_likelycatchhow
* developingriskwho
  - utter_developingriskwho
* catchfrompet
  - utter_catchfrompet
* survivelongdoes
  - utter_survivelongdoes
* contractsymptomsshould
  - utter_contractsymptomsshould
* precautionsqaurantinetaken
  - utter_precautionsqaurantinetaken
* protectshouldmyself
  - utter_protectshouldmyself
* knowhavehow
  - utter_knowhavehow
* hydroxychloroquinecureis
  - utter_hydroxychloroquinecureis
* spreaddoeshow
  - utter_spreaddoeshow
* outsidesafeis
  - utter_outsidesafeis
* humansspreadthis
  - utter_humansspreadthis
* shouldtestedfor
  - utter_shouldtestedfor
* testedwherecan
  - utter_testedwherecan
* communityoutbreakshould
  - utter_communityoutbreakshould
* cleaningproductsprotect
  - utter_cleaningproductsprotect
* differentsymptomschildren
  - utter_differentsymptomschildren
* contactsomeoneshould
  - utter_contactsomeoneshould
* patientsdonateblood
  - utter_patientsdonateblood
* internationalpackagesrecieve
  - utter_internationalpackagesrecieve
* seeingcasesrise
  - utter_seeingcasesrise
* conditionscovid19what
  - utter_conditionscovid19what


* goodbye
  - utter_goodbye


