��    {      �  �   �      h
  =  i
  .   �  �   �  �   k     �     �     	          0     C    \  [   i     �  
   �  	   �     �                     :  #   L     p     �     �     �     �     �     �      �     �                $     E  '   N     v     �  (   �  %   �     �  	   �  *        ,     L     Q     p          �     �  5   �     �  
   �     �               +     9     ?     O     d  	   z  #   �     �     �     �     �     �     �     �     �     �       1     -   G  ,   u  *   �     �     �     �     �     �       ?     u   R     �  
   �     �     �               ,     5     :     >     C     L     [     `     f     o     �     �     �     �  $   �               6     E     [     r     �     �     �  !   �  *   �  7        W  #   l  	   �     �     �  c  �  �    8   �  �   ,  �   �     �     �     �  =   �     �     �  �    ~   �     ,  
   >     I  7   P  #   �  #   �  0   �        0         F      a      |   '   �      �      �      �   5   �      !     7!     I!  *   V!     �!  3   �!     �!     �!  A   �!  J   "     ^"  
   u"  6   �"  '   �"     �"  )   �"     #     5#     L#     ^#  `   p#     �#     �#  1   �#  
   )$     4$     H$  
   Z$     e$  6   y$  D   �$     �$  2   %     8%     =%  0   I%     z%     �%     �%     �%     �%     �%     �%  :   &  8   <&  <   u&  ;   �&     �&     �&     '  )   '     H'  
   g'  ^   r'  �   �'     �(     �(  !   �(     �(     �(      �(     )     +)     2)  
   N)     Y)     m)     �)     �)     �)     �)     �)  8   �)  9   -*     g*  7   }*  0   �*  -   �*     +     -+  )   C+  *   m+  *   �+     �+     �+  :   �+  ?   ),  a   i,     �,  <   �,      -  #   0-     T-     S   O   7         *   6      %       s          ]       ;       \   W           &   5   T   !   ,   l   D      H   A       ^          -   q       V       e   `                             Y   .          /   X   0                _   2   @   k   g   (   3      n      v   :   E          [   '             #              >   9   {   x       P   o   =           4   Q   "       j       F   <       r   a      R       1   b   I                        p           z       y   
   +      h   U   G       B   C   m           M           8   f   i          	   c   u   L      Z      J       $      K          N       t   d           ?   )   w    A JSON document to include in the request. Can also be a template that return a JSON document. Templates receive the workflow log entry instance as part of their context via the variable "entry_log". The "entry_log" in turn provides the "workflow_instance", "datetime", "transition", "user", and "comment" attributes. A link to the entire history of this workflow. API URL pointing to a document type in relation to the workflow to which it is attached. This URL is different than the canonical document type URL. API URL pointing to a workflow in relation to the document to which it is attached. This URL is different than the canonical workflow URL. Action Action type Actions Actions for workflow state: %s Additional details Available document types Can be an IP address, a domain or a template. Templates receive the workflow log entry instance as part of their context via the variable "entry_log". The "entry_log" in turn provides the "workflow_instance", "datetime", "transition", "user", and "comment" attributes. Comma separated list of document type primary keys to which this workflow will be attached. Comment Completion Condition Create a "%s" workflow action Create action Create state Create states for workflow: %s Create transition Create transitions for workflow: %s Create workflow Create workflows Current state Current state of a workflow Date and time Datetime Delete Delete workflow state action: %s Delete workflows Destination state Detail Detail of workflow: %(workflow)s Document Document "%s" transitioned successfully Document states Document types Document types assigned the workflow: %s Document types assigned this workflow Document workflows Documents Documents in the workflow "%s", state "%s" Documents with the workflow: %s Edit Edit workflow state action: %s Edit workflows Enabled Entry action data Entry action path Error updating workflow transition trigger events; %s Event trigger: %s Event type Execute workflow tools Initial Initial state Internal name Label Last transition Launch all workflows Launch all workflows? Namespace New workflow state action selection No None Not a valid transition choice. On entry On exit Origin state Password Payload Preview Preview of: %s Primary key of the destination state to be added. Primary key of the document type to be added. Primary key of the origin state to be added. Primary key of the transition to be added. Required Select State documents States States of workflow: %s Submit The dotted Python path to the workflow action class to execute. This value will be used by other apps to reference this workflow. Can only contain letters, numbers, and underscores. Timeout Transition Transition triggers Transition workflows Transitions Transitions of workflow: %s Triggers Type URL User Username View workflows When When? Workflow Workflow documents Workflow instance Workflow instance log entries Workflow instance log entry Workflow instances Workflow launch queued successfully. Workflow runtime proxies Workflow runtime proxy Workflow state Workflow state action Workflow state actions Workflow state runtime proxies Workflow state runtime proxy Workflow states Workflow transition Workflow transition trigger event Workflow transition trigger events for: %s Workflow transition trigger events updated successfully Workflow transitions Workflow transitions trigger events Workflows Workflows for document: %s Yes Project-Id-Version: Mayan EDMS
Report-Msgid-Bugs-To: 
PO-Revision-Date: 2020-09-27 06:46+0000
Last-Translator: Roberto Rosario
Language-Team: Persian (http://www.transifex.com/rosarior/mayan-edms/language/fa/)
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
Language: fa
Plural-Forms: nplurals=2; plural=(n > 1);
 یک سند JSON برای درخواست در همچنین می تواند یک الگو باشد که یک سند JSON را بازگرداند. قالب ها ورودی ورودی ورود به سیستم را به عنوان بخشی از متن خود از طریق متغیر "entry_log" دریافت می کنند. "entry_log" به نوبه خود ویژگی های "workflow_instance"، "datetime"، "transition"، "user" و "comment" را فراهم می کند. لینک به کل تاریخچه این گردش کار URL API اشاره به نوع سند مربوط به جریان کاری که به آن متصل است. این URL متفاوت از URL سند نوع سند است. URL API اشاره به یک گردش کار در رابطه با سند که آن متصل است. این URL متفاوت از URL کارآفرینی کانونی است. عمل نوع اقدام اقدامات اقدامات مربوط به وضعیت گردش کار: %s جزئیات اضافی نوع سند موجود می تواند یک آدرس IP، یک دامنه یا یک الگو باشد. قالب ها ورودی ورودی ورود به سیستم را به عنوان بخشی از متن خود از طریق متغیر "entry_log" دریافت می کنند. "entry_log" به نوبه خود ویژگی های "workflow_instance"، "datetime"، "transition"، "user" و "comment" را فراهم می کند. لیست کاملی از نوع سند کپی اولیه که این جریان کار متصل است، جدا شده است. اظهار نظر تکمیل شرط یک اقدام عملیاتی "%s" ایجاد کنید اقدام را ایجاد کنید ایجاد وضعیت یا حالت ایجاد حالت برای گردش کار: %s ایجاد گذار ایجاد گذار برای گردش کار: %s ایجاد گردش کار ایجاد گردش کار وضعیت فعلی وضعیت فعلی جریان کاری تاریخ و زمان زمان قرار حذف عمل عملکرد دولت را حذف کنید: %s حذف جریان کار حالت مقصد جزئیات جزئیات گردش کار: %(workflow)s سند سند "%s" با موفقیت انتقال یافت سند نوع سند انواع سند گردش کار را تعیین می کند: %s انواع سند این جریان کاری را تعیین می کنند گردش کار سند اسناد اسناد در جریان کار "%s"، حالت "%s" اسناد با جریان کاری: %s ویرایش ویرایش عمل جریان کار: %s ویرایش جریان کار فعال شده است Entry action data Entry action path خطا در به روز رسانی وقایع رویداد انتقال جریان کاری؛ %s Event trigger: %s نوع رویداد ابزار گردش کار را اجرا کنید اولیه حالت اولیه نام داخلی برچسب آخرین گذار راه اندازی تمام جریانهای کاری همه جریانهای کاری را راه اندازی کنید؟ فضای نام انتخاب عملکرد عمل جدید دولت نه هیچ یک یک انتخاب منتخب معتبر نیست در ورودی در خروج کشور مبدا کلمه عبور ظرفیت ترابری پیش نمایش پیش نمایش از: %s کلید اصلی کشور مقصد اضافه می شود کلید اولیه نوع سند اضافه می شود کلید اولیه حالت مبدأ اضافه می شود کلید اصلی انتقال برای اضافه کردن الزامی انتخاب اسناد دولتی و یا وضعیتها حالات  States ایالت گردش کار: %s ارسال مسیر پایتون نقطه به کلاس عملیات گردش کار برای اجرای. این مقدار توسط برنامه های دیگر برای ارجاع به این گردش کار استفاده می شود. فقط شامل حروف، اعداد و حروف الفبا است. وقفه گذار باعث انتقال می شود جریان کار انتقال گذار انتقال گردش کار: %s راه اندازی نوع نشانی اینترنتی کاربر نام کاربری مشاهده جریان کار چه زمانی چه زمانی؟ گردش کار اسناد گردش کار نمونه گردش کار ورودیهای لگ یک مورد از گردش کار ورودی به لاگ یک مورد از گردش کار نمونه کارها راه اندازی کار در صف با موفقیت. پروکسی کارآمد در زمان اجرا پروکسی زمانبندی گردش کار حالت گردش کار Workflow state action اقدامات دولت کار جریان پروکسی زمان اجرا وضعیت  پروکسی زمان اجرا وضعیت  وضعیت کار گذار گردش کار رویداد رویداد انتقال جریان کاری حوادث ماژول انتقال گردش کار برای: %s رویدادهای رویداد انتقال جریان کار با موفقیت به روز شد گذارهای کاری انتقال گردش کار باعث وقایع می شود گردش کار گردش کار برای سند: %s بله 