# complexity = j['complexity']

        # unit = j['type'] + ' : ' # + # j['classname']

        # classification = j['rank']
        # startLineNumber = j['lineno']
        # endLineNumber = j['endline']
        # # sloc = endLineNumber - startLineNumber

        # # metric = {}
        # # metric['complexity'] = complexity
        # # metric['unit'] = unit
        # # metric['classification'] = classification
        # # metric['file'] = filename
        # # metric['startLineNumber'] = startLineNumber
        # # metric['endLineNumber'] = endLineNumber
        # # # metric['sloc'] = sloc
        # # metrics.append(metric)



# for metric in metrics:
#     # print metric
#     print '<metric>'
#     print '  <complexity>%s</complexity>' % metric['complexity']
#     print '  <unit>%s</unit>' % metric['unit']
#     print '  <classification>%s</classification>' % metric['classification']
#     print '  <file>%s</file>' % metric['file']
#     print '  <startLineNumber>%s</startLineNumber>' % metric['startLineNumber']
#     print '  <endLineNumber>%s</endLineNumber>' % metric['endLineNumber']
#     print '  <SLOC>%s</SLOC>' % metric['sloc']
#     print '</metric>'

# complexity = ''
# unit = ''
# classification = ''
# filename = ''
# startLineNumber = ''
# endLineNumber = ''
# sloc = ''


# {
#     'complexity': complexity,
#     'unit': unit,
#     'classification': classification,
#     'file': filename,
#     'startLineNumber': startLineNumber,
#     'endLineNumber': endLineNumber,
#     'sloc': sloc
# }

# public static string GetClassification(int ccm)
#     {
#       if (ccm >= 51)
#         return "untestable, very high risk";
#       if (ccm >= 21)
#         return "complex, high risk";
#       else if (ccm >= 11)
#         return "more complex, moderate risk";
#       else
#         return "simple, without much risk";
#     }


# Console.WriteLine("  <metric>");
# Console.WriteLine("    <complexity>{0}</complexity>", metric.CCM);
# Console.WriteLine("    <unit>{0}</unit>", XmlOutputter.XmlAdjust(metric.Unit));
# Console.WriteLine("    <classification>{0}</classification>", metric.Classification);
# Console.WriteLine("    <file>{0}</file>", metric.Filename);
# Console.WriteLine("    <startLineNumber>{0}</startLineNumber>", metric.StartLineNumber);
# Console.WriteLine("    <endLineNumber>{0}</endLineNumber>", metric.EndLineNumber);
# Console.WriteLine("    <SLOC>{0}</SLOC>", (metric.EndLineNumber - metric.StartLineNumber).ToString());
# Console.WriteLine("  </metric>");


# Driver::HandleDirectory(string basePath,string path) : 7 - simple, without much risk (\Driver.cs@line 141)
 # public bool IsValidFile(string filename)
 #    {
 #      if (this.configFile != null)
 #      {
 #        foreach (string name in this.configFile.ExcludeFiles)
 #        {
 #          if (filename.ToLower().Contains(name.ToLower()))
 #            return false;
 #        }
 #      }
# Driver::IsValidFile(string filename) : 6 - simple, without much risk (\Driver.cs@line 84)
# Program::CreateConfigurationFromArgs(string [ ] args) : 6 - simple, without much risk (\Program.cs@line 71)
# Driver::PathShouldBeExcluded(string path) : 5 - simple, without much risk (\Driver.cs@line 109)
# XmlOutputter::Output(List<ccMetric>metrics,List<ErrorInfo>errors,bool verbose) : 5 - simple, without much risk (\XmlOutputter.cs@line 17)
# ConsoleOutputter::Output(List<ccMetric>metrics,List<ErrorInfo>errors,bool verbose) : 4 - simple, without much risk (\ConsoleOutputter.cs@line 12)
# Driver::AnalyzeFilestream(object context) : 4 - simple, without much risk (\Driver.cs@line 47)
# TabbedOutputter::Output(List<ccMetric>metrics,List<ErrorInfo>errors,bool verbose) : 4 - simple, without much risk (\TabbedOutputter.cs@line 12)
# Program::OutputterFactory(string outputType) : 3 - simple, without much risk (\Program.cs@line 60)
# Program::ValidateArgs(string [ ] args) : 2 - simple, without much risk (\Program.cs@line 15)
# Program::LoadConfiguration(string [ ] args) : 2 - simple, without much risk (\Program.cs@line 97)
# Program::Main(string [ ] args) : 2 - simple, without much risk (\Program.cs@line 122)

# Console.WriteLine("{0} : {1} - {2} ({3}@line {4})",
#           metric.Unit, metric.CCM, metric.Classification, metric.Filename, metric.StartLineNumber);
