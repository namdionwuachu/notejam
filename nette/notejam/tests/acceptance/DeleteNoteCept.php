<?php
$I = new AcceptanceTester($scenario);
$I->wantTo('delete note');
//$I->amOnPage('/notes/5/delete');
//$I->seeResponseCodeIs(404); // This will work only in production mode
$I->testLogin();
$I->amOnPage('/notes/1/delete');
$I->click('Yes, I want to delete this note');
$I->dontSee('Note 1');
