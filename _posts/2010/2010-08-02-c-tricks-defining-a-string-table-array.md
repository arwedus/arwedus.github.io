---
title: "C Tricks: Defining a String Table (Array)"
date: "2010-08-02"
categories:
  - "programming"
  - "C and C++"
tags:
  - "array-of-strings"
  - "string-table"
layout: post
lang: en
---

Sometimes you need a String Table - an array of predefined character arrays - in C. There is the simple way to do this, by defining a fixed string size and table size:

```c
#define TABLESIZE 3 #define STRINGSIZE 16 char stringTable[TABLESIZE][STRINGSIZE] = { "Entry1", "Entry2", "Entry3" };
```

However, there is a far more elegant way:

```c
char * stringTable[] = { "Entry1", "Entry2", "Entry3", "verylongEntryonlytotestifithasanyinfluenceonsizeof"}; printf("String table size: %d \n", sizeof(stringTable)/sizeof(char*) );
```

This will output "String table size: 4" just as you intended. You do not have to worry about adjusting your defines whenever you make changes to the string table. Also, you do not waste memory because every character array only takes up as much space as needed for the particular string.

p.s.: I hope this actually works in C, I only tested it with a C++ compiler.
