public class iglogger {
    // Change this as needed. This is the default log message string
    // In logcat, set your filter for "tag:!!!" to view the messages from this class
    private static String LOG_TAG = "IGLogger";
    private static String TRACE_TAG = "IGTraceLogger";
    private static String VERSION = "IGLogger 2.55 - 04/24/2013";

    /* Trace Method
     *  - Use this call to just print you where here in a method
     *  - Main use is for putting this at the start of each method to help trace an obfuscated app
     *
     * *** SMALI CODE TO ADD ***
     * invoke-static {}, Lcom/7a6ac0/iglogger;->trace_method()I
     *
     */
    static public int trace_method() {
        Throwable t = new Throwable();
        String logtag = "Method: " + t.getStackTrace()[1].getClassName();

        // Unfortuantely we cant get the details for an overloaded method
        // this would be helpful for obfuscated classes
        logtag = logtag + "->" + t.getStackTrace()[1].getMethodName();

        // Line number so far as "-1" but this might work on some apps.
        // We'll leave it for now.
        logtag = logtag + " Line " + t.getStackTrace()[1].getLineNumber();
        return android.util.Log.i(LOG_TAG, logtag);
    }

}
