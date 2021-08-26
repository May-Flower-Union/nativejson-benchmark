# Conformance of Qajson4c (C)

## 1. Parse Validation


Summary: 34 of 34 are correct.

## 2. Parse Double


Summary: 66 of 66 are correct.

## 3. Parse String


Summary: 9 of 9 are correct.

## 4. Roundtrip

* Fail:
~~~js
[5e-324]
~~~

~~~js
[0.0]
~~~

* Fail:
~~~js
[2.225073858507201e-308]
~~~

~~~js
[0.0]
~~~

* Fail:
~~~js
[2.2250738585072014e-308]
~~~

~~~js
[0.0]
~~~

* Fail:
~~~js
[1.7976931348623157e308]
~~~

~~~js
[1.797693e+308]
~~~


Summary: 23 of 27 are correct.

