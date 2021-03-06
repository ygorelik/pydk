### 2019-06-25 version 0.5.5.post2

#### Python

##### Enhancements
 * Add function to return difference between two YDK Objects of the same type ([#925](https://github.com/CiscoDevNet/ydk-gen/issues/925))
 * Add function to return Enum object from type and value ([#926](https://github.com/CiscoDevNet/ydk-gen/issues/926))
 * Add YDK Meta Data for must and when statements in a contaner ([#927](https://github.com/CiscoDevNet/ydk-gen/issues/927))

##### Bug fixes
 * Fix ydk-gen to handle multiple augments ([#922](https://github.com/CiscoDevNet/ydk-gen/issues/922))
 * Navigate xpath is not covered if the middle path is a list and has more than 2 items ([#928](https://github.com/CiscoDevNet/ydk-gen/issues/928))
 * YDK-0.5.5: generated bundle code fails initialize leaves of type bits ([#936](https://github.com/CiscoDevNet/ydk-gen/issues/936))


### 2019-03-26 version 0.5.5.post1

#### Python

##### Enhancements
 * adding new operations, merge, replace, remove [#816](https://github.com/CiscoDevNet/ydk-gen/issues/816))
 * Add _is_present attribute in present container meta data [#896](https://github.com/CiscoDevNet/ydk-gen/issues/896))
 * YDK MetaInfo should have a field for mandatory leaf ([#918](https://github.com/CiscoDevNet/ydk-gen/issues/918))

##### Bug fixes
 * The deepcopy of YLeafList changes type of member elements ([#904](https://github.com/CiscoDevNet/ydk-gen/issues/904))
 * Fix deepcopy usage with CRUD ([#908](https://github.com/CiscoDevNet/ydk-gen/issues/908))
 * Max value of range is set to None when not specified in the Yang model ([#916](https://github.com/CiscoDevNet/ydk-gen/issues/916))


### 2017-06-06 version 0.5.5

#### Python
 * Fixed bundle `setup.py` to match ydk `core` dependency in bundle profile ([#433](https://github.com/CiscoDevNet/ydk-gen/issues/443))
 * Updated `lxml` dependency for ydk `core` package ([#427](https://github.com/CiscoDevNet/ydk-gen/issues/427))
 * Improved reading of data using `ExecutorService` ([#332](https://github.com/CiscoDevNet/ydk-gen/issues/332)) and `CRUDService` ([#457](https://github.com/CiscoDevNet/ydk-gen/issues/457))
 * Fixed encoding key elements of yang `list`s ([#363](https://github.com/CiscoDevNet/ydk-gen/issues/363)) and operational data ([#452](https://github.com/CiscoDevNet/ydk-gen/issues/452), [#455](https://github.com/CiscoDevNet/ydk-gen/issues/455))

#### C++
 * Added equality operator for model API objects ([#432](https://github.com/CiscoDevNet/ydk-gen/pull/432))
 * Improved handling of presence `container`s ([#437](https://github.com/CiscoDevNet/ydk-gen/pull/437))

#### ydk-gen
 * Added [`cisco-ios-xe` bundle](https://github.com/CiscoDevNet/ydk-gen/blob/master/profiles/bundles/cisco-ios-xe_16_5_1.json) to support Cisco IOS XE 16.5.1 release
 * Improved exception handling in the ydk-gen `generate.py` script ([#440](https://github.com/CiscoDevNet/ydk-gen/pull/440))

#### Documentation
 * Improved getting-started guides for YDK-Py and YDK-Cpp  ([#418](https://github.com/CiscoDevNet/ydk-gen/pull/418), [#419](https://github.com/CiscoDevNet/ydk-gen/pull/419))
 * Made table of contents for bundle documentation be sorted alphabetically ([#446](https://github.com/CiscoDevNet/ydk-gen/pull/418), [#419](https://github.com/CiscoDevNet/ydk-gen/pull/446))
 * Improved documentation of `rpc` classes ([#435](https://github.com/CiscoDevNet/ydk-gen/issues/435))

### 2017-03-17 version 0.5.4

#### Python
 * Improved logging to indicate message directionality ([#388](https://github.com/CiscoDevNet/ydk-gen/pull/388))
 * Provide more details for validation error message for leaf-lists ([#398](https://github.com/CiscoDevNet/ydk-gen/pull/398))
 * Remove indirect python requirements from `setup.py` ([#392](https://github.com/CiscoDevNet/ydk-gen/pull/392))
 * If validation error occurs when decoding payload, include payload as an attribute of the `YPYModelError` raised ([#381](https://github.com/CiscoDevNet/ydk-gen/pull/381))
 * Update Python package generation and post YDK-Py on the Python package index - PyPi ([#404](https://github.com/CiscoDevNet/ydk-gen/issues/404), [#406](https://github.com/CiscoDevNet/ydk-gen/issues/406))

#### C++
 * Changed dependent libraries ([#382](https://github.com/CiscoDevNet/ydk-gen/pull/382))
   * Use header-only [spdlog](https://github.com/gabime/spdlog) library for logging
   * Use header-only [catch](https://github.com/philsquared/Catch) library for testing
   * Completely remove boost dependency
 * Create default yang models repository for each bundle. Install yang models as part of bundle shared library ([#292](https://github.com/CiscoDevNet/ydk-gen/pull/292))
   * Make passing in `path::Repository` object optional for `CodecServiceProvider`
 * Fix issue with handling augmented leafs in `CrudService` ([#351](https://github.com/CiscoDevNet/ydk-gen/pull/351))
 * Use smart pointers (like `shared_ptr`) in place of raw pointers ([#382](https://github.com/CiscoDevNet/ydk-gen/pull/382)), ([#393](https://github.com/CiscoDevNet/ydk-gen/pull/393))
 * Support linking to multiple bundles ([#349](https://github.com/CiscoDevNet/ydk-gen/pull/349))
 * Added sample code for using YDK with JSON configs in combination with CRUD service ([#387](https://github.com/CiscoDevNet/ydk-gen/pull/387))

#### ydk-gen
 * Improved generation of C++ code to consume less compile-time memory for large yang models ([#386](https://github.com/CiscoDevNet/ydk-gen/pull/386)), ([#336](https://github.com/CiscoDevNet/ydk-gen/pull/336))
 * Add check for valid profile file to ydkgen ([#378](https://github.com/CiscoDevNet/ydk-gen/pull/378))
 * Added code coverage for C++ code ([#373](https://github.com/CiscoDevNet/ydk-gen/pull/373))
 * Updated [`cisco-ios-xr` bundle](https://github.com/CiscoDevNet/ydk-gen/blob/master/profiles/bundles/cisco-ios-xr_6_2_1.json) to support Cisco IOS XR 6.2.1 release

#### Documentation
 * Separated top data classes from type classes in table of contents ([#372](https://github.com/CiscoDevNet/ydk-gen/pull/372))
 * Fixed ydk version not being correctly printed for C++ documentation ([#374](https://github.com/CiscoDevNet/ydk-gen/pull/374))
 * Indicate bundle version in C++ and python bundle documentation ([#383](https://github.com/CiscoDevNet/ydk-gen/pull/383))

### 2017-01-30 version 0.5.3

#### Python

* Fixed issues with netconf service ([#323](https://github.com/CiscoDevNet/ydk-gen/issues/323), [#305](https://github.com/CiscoDevNet/ydk-gen/issues/305))
* Disambiguated model API classes called 'None' ([#318](https://github.com/CiscoDevNet/ydk-gen/issues/318))
* Removed 'Bits' from classes representing bits leafs ([#318](https://github.com/CiscoDevNet/ydk-gen/issues/318), [#320](https://github.com/CiscoDevNet/ydk-gen/issues/320))

#### C++

* Introduced support for two new service providers ([#365](https://github.com/CiscoDevNet/ydk-gen/pull/365))
  * RestconfServiceProvider
  * OpenDaylightServiceProvider
* Introduced support for netconf service ([#341](https://github.com/CiscoDevNet/ydk-gen/pull/341), [#352](https://github.com/CiscoDevNet/ydk-gen/pull/352))
* Released ydk-cpp for OSX platform (on [Homebrew](https://github.com/CiscoDevNet/homebrew-ydk)) and on Ubuntu platform (on [Lauchpad](https://launchpad.net/~ydk)) ([#362](https://github.com/CiscoDevNet/ydk-gen/pull/362), [#322](https://github.com/CiscoDevNet/ydk-gen/pull/322))
* Added support for generated CRUD model tests based on bundles ([#354](https://github.com/CiscoDevNet/ydk-gen/pull/354))
* Improved negative test cases and added support for netconf operations on leafs and leaf-lists ([#324](https://github.com/CiscoDevNet/ydk-gen/pull/324))

#### Documentation

* Added documentation with examples for C++ OpenDaylightServiceProvider and RestconfServiceProvider ([#365](https://github.com/CiscoDevNet/ydk-gen/pull/365))
* Included model revision in documentation ([#272](https://github.com/CiscoDevNet/ydk-gen/issues/272))
* Improved documentation for string leafs ([#346](https://github.com/CiscoDevNet/ydk-gen/issues/346)), decimal64 leafs ([#300](https://github.com/CiscoDevNet/ydk-gen/issues/300), [#294](https://github.com/CiscoDevNet/ydk-gen/issues/294))
* Added more detailed documentation for ydk-gen ([#335](https://github.com/CiscoDevNet/ydk-gen/pull/335), [#364](https://github.com/CiscoDevNet/ydk-gen/pull/364))
* Improved look and feel of documentation ([#361](https://github.com/CiscoDevNet/ydk-gen/pull/361), [#356](https://github.com/CiscoDevNet/ydk-gen/pull/356))
* Cleaned up unused bundle profiles and added READMEs ([#208](https://github.com/CiscoDevNet/ydk-gen/issues/208))

### 2016-11-30 version 0.5.2

#### Python

* CRUD service / Codec service / Netconf service improvements
  * Improved error handling for mismatched model API types ([#241](https://github.com/CiscoDevNet/ydk-gen/issues/241))
  * Fixed issues with certain operations in netconf service ([#247](https://github.com/CiscoDevNet/ydk-gen/issues/247), [#248](https://github.com/CiscoDevNet/ydk-gen/issues/248), [#252](https://github.com/CiscoDevNet/ydk-gen/issues/252), [#235](https://github.com/CiscoDevNet/ydk-gen/issues/235))
  * Fixed issue with CRUD service identityref keys ([#257](https://github.com/CiscoDevNet/ydk-gen/issues/257))

* Bundle improvements
  * Made generate.py executable ([#227](https://github.com/CiscoDevNet/ydk-gen/issues/227))
  * Removed auto capitalization of enum literals ([#230](https://github.com/CiscoDevNet/ydk-gen/issues/230))
  * Updated [`cisco-ios-xr` bundle](https://github.com/CiscoDevNet/ydk-gen/blob/master/profiles/bundles/cisco-ios-xr_6_1_2.json) to support Cisco IOS XR 6.1.2 release ([#316](https://github.com/CiscoDevNet/ydk-gen/pull/316))
  
* Logging improvements
  * Improved logging for services and providers ([#251](https://github.com/CiscoDevNet/ydk-gen/issues/251), [#254](https://github.com/CiscoDevNet/ydk-gen/issues/254), [#280](https://github.com/CiscoDevNet/ydk-gen/issues/280), [#283](https://github.com/CiscoDevNet/ydk-gen/issues/283), [#284](https://github.com/CiscoDevNet/ydk-gen/issues/284))

* Documentation improvements
  * Added YDK logos and reorganized to be more readable ([#301](https://github.com/CiscoDevNet/ydk-gen/pull/301), [#296](https://github.com/CiscoDevNet/ydk-gen/pull/296), [#289](https://github.com/CiscoDevNet/ydk-gen/pull/289))
  * Improved documentation of YANG attributes like data type (configuration or state), default value, units, status etc ([#249](https://github.com/CiscoDevNet/ydk-gen/issues/249), [#290](https://github.com/CiscoDevNet/ydk-gen/issues/290))  
  * Improved netconf service documentation ([#235](https://github.com/CiscoDevNet/ydk-gen/issues/235))

#### C++ (alpha)

* Introduced support for C++ YDK bindings ([issue#118](https://github.com/CiscoDevNet/ydk-gen/issues/118), related [commits](https://github.com/manradhaCisco/ydk-gen/commits/ydk_core) and [pull requests](https://github.com/manradhaCisco/ydk-gen/pulls?q=is%3Apr+is%3Aclosed))
* Added support for CRUD, Validation and Codec services, along with Netconf and Codec providers, YDK types and errors
* Added support for Path API
* Used libyang and libnetconf libraries as part of the service and provider abstraction layer  
* Integrated with CMake build system
* Wrote unit tests using `boost::unit_test`
* Added support for logging using `boost::log`
* Added documentation using `sphinx`
* Integrated C++ testing into CI using travis-ci ([#286](https://github.com/CiscoDevNet/ydk-gen/issues/286))

### 2016-10-10 version 0.5.1

* Support for Python3
  * Introduced support for Python 3 ([#60](https://github.com/CiscoDevNet/ydk-gen/issues/60))
  * Both Python 2 and Python 3 are now supported for `ydk-gen` and `ydk-py`

* Bundle improvements
  * Improved usage of import statements in YDK model API to reduce chances of circular import dependency ([#216](https://github.com/CiscoDevNet/ydk-gen/issues/216))
  * Updated [`cisco-ios-xr` bundle](https://github.com/CiscoDevNet/ydk-gen/blob/master/profiles/bundles/cisco-ios-xr_6_1_1.json) to support Cisco IOS XR 6.1.1 release ([#258](https://github.com/CiscoDevNet/ydk-gen/pull/258))
  * Updated [`openconfig` bundle](https://github.com/CiscoDevNet/ydk-gen/blob/master/profiles/bundles/openconfig_0_1_1.json) ([#258](https://github.com/CiscoDevNet/ydk-gen/pull/258))

* Documentation improvements
  * Improved documentation for bundle installation ([#244](https://github.com/CiscoDevNet/ydk-gen/pull/244))
  * Added documentation for executor service ([#263](https://github.com/CiscoDevNet/ydk-gen/pull/263))

### 2016-08-03 version 0.5.0
 * Introduced YDK bundles ([#43](https://github.com/CiscoDevNet/ydk-gen/issues/43), [#148](https://github.com/CiscoDevNet/ydk-gen/issues/148), [#149](https://github.com/CiscoDevNet/ydk-gen/issues/149))
  * Created YDK core library and pluggable namespace packages that share the same module prefix `ydk.models`
  * Generated documentation for YDK core and bundles

* CRUD service / Codec service / Netconf service improvements
  * Improved support for presence containers, nested enum and identity classes ([#169](https://github.com/CiscoDevNet/ydk-gen/pull/169))
  * Improved support for lists with multiple keys by ensuring that the order of keys is preserved ([#179](https://github.com/CiscoDevNet/ydk-gen/issues/179))
  * Improved support for leaf-list of identity type ([#186](https://github.com/CiscoDevNet/ydk-gen/issues/186))
  * Added check for user error which can occur when self-referencing YDK object as parent object ([#184](https://github.com/CiscoDevNet/ydk-gen/issues/184))
  * Improved error-reporting for commit-time error ([#190](https://github.com/CiscoDevNet/ydk-gen/issues/190))
  * Fixed CRUD read support for modules containing top-level list ([#194](https://github.com/CiscoDevNet/ydk-gen/issues/194))

* Testing improvements
  * Added Mac OS X installation and running codec service sanity tests to CI ([#175](https://github.com/CiscoDevNet/ydk-gen/pull/175))

* Documentation improvements
  * Indicated mandatory leafs in the documentation ([#177](https://github.com/CiscoDevNet/ydk-gen/issues/177))
  * Specified path to referred leaf for leafrefs ([#177](https://github.com/CiscoDevNet/ydk-gen/issues/177))
  * Fix documentation of presence containers ([#192](https://github.com/CiscoDevNet/ydk-gen/issues/192))
  * Enhanced documentation of leafs of identityref type by indicating all the subclasses of identity base class referred to by the identityref ([#161](https://github.com/CiscoDevNet/ydk-gen/issues/161))
  * Added documentation on how to use YDK delete operation and improved documentation for YDK read operation ([#204](https://github.com/CiscoDevNet/ydk-gen/pull/204))

### 2016-06-17 version 0.4.2
 * Error handling improvements
  * Fixed local validation to correctly check for types and values ([#116](https://github.com/CiscoDevNet/ydk-gen/issues/116))
  * Introduced error hierarchy to represent errors from various components, viz.: YPYModelErrors, YPYServiceError, YPYServiceProviderError ([#133](https://github.com/CiscoDevNet/ydk-gen/issues/133))
    * When raising YPYModelErrors, include errors dictionary with key as path to data, and value as tuple of error code and error message
  * Added more extensive negative test cases to ydk-gen to test handling of error ([#134](https://github.com/CiscoDevNet/ydk-gen/issues/134))
 * CRUD service / Codec service / Netconf service provider improvements
  * Added support for multiple objects to codec service ([#122](https://github.com/CiscoDevNet/ydk-gen/issues/122))
  * Added logging for codec service ([#97](https://github.com/CiscoDevNet/ydk-gen/issues/97))
  * Have logging hierarchy automatically follow package hierarchy ([#100](https://github.com/CiscoDevNet/ydk-gen/issues/100))
  * Have netconf service return YDK python objects instead of XML strings ([#120](https://github.com/CiscoDevNet/ydk-gen/issues/120))
  * Fixed decoding issue with leaf-list of enums ([#150](https://github.com/CiscoDevNet/ydk-gen/issues/150))
 * Removed requirements.txt from ydk-py and added all requirements to setup.py
 * Enforce PEP8 naming for Identity classes ([#152](https://github.com/CiscoDevNet/ydk-gen/issues/152))
 * Added full ydk-py version to the documentation ([#144](https://github.com/CiscoDevNet/ydk-gen/issues/144))

### 2016-05-20 version 0.4.1
 * Added openconfig bgp-policy APIs to ydk-py ([#102](https://github.com/CiscoDevNet/ydk-gen/issues/102))
 * Introduced ability to programmatically retrieve SDK version of ydk-py ([#8](https://github.com/CiscoDevNet/ydk-gen/issues/8))
 * Removed unused dependencies from ydk-py's requirements.txt ([#48](https://github.com/CiscoDevNet/ydk-gen/issues/48))
 * Introduced [coveralls](https://coveralls.io) and improved [travis CI](https://travis-ci.org) integration for ydk-gen github ([#84](https://github.com/CiscoDevNet/ydk-gen/issues/84), [#54](https://github.com/CiscoDevNet/ydk-gen/issues/54), [#15](https://github.com/CiscoDevNet/ydk-gen/issues/15), [#46](https://github.com/CiscoDevNet/ydk-gen/issues/46))
 * CRUD service / Netconf service provider improvements
  * Added timeout parameter to NetconfServiceProvider ([#1](https://github.com/CiscoDevNet/ydk-gen/issues/1))
  * Fixed issues with decoding leafs of union type and nodes defined in sub-modules  ([#5](https://github.com/CiscoDevNet/ydk-gen/issues/5), [#56](https://github.com/CiscoDevNet/ydk-gen/issues/56))
  * Fixed issue with encoding enums, identities defined in external modules ([#30](https://github.com/CiscoDevNet/ydk-gen/issues/30), [#103](https://github.com/CiscoDevNet/ydk-gen/issues/103))
  * Improved support for deleting leafs, leaf-lists and lists ([#55](https://github.com/CiscoDevNet/ydk-gen/issues/55), [#103](https://github.com/CiscoDevNet/ydk-gen/issues/103))
 * Documentation improvements
  * Added 'About ydk-py' page with information about ydk-gen used to generate ydk-py ([#6](https://github.com/CiscoDevNet/ydk-gen/issues/6))
  * Indicate in documentation YDK class attributes that are keys ([#41](https://github.com/CiscoDevNet/ydk-gen/issues/41))
  * Made top containers show up at the top of the table of contents for every module document ([#39](https://github.com/CiscoDevNet/ydk-gen/issues/39))

### 2016-04-15 version 0.4.0

  * Introduced netconf service and codec service
    * Netconf service provides APIs to execute netconf operations
    * Codec service provides APIs to encode python objects and decode payloads
  * Support for yang deviation
  * Support for subscribing to model-driven telemetry
  * Logging made more consistent
    * CRUDService outputs type of operation
    * When logging is enabled, all NETCONF messages are logged including commit
    * Log messages at various stages (send RPC request, receive reply, commit 
      etc) instead of logging all at once at the end
  * Updated enums in YDK classes to use enum34
    * Improved enum documentation
  * Improved error reporting for ydk-py and ydk-gen

### 2016-03-11 version 0.3.0:

  * First public release.
