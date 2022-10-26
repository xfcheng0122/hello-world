//println(Jenkins.instance.pluginManager.plugins)
//println(Jenkins.instance)
//println(Jenkins.instance.metaClass.methods*.name)
import hudson.util.RemotingDiagnostics
import jenkins.model.Jenkins

String agentName = 'centos8'
//groovy script you want executed on an agent
groovy_script = '''
println System.getenv("PATH")
println "uname -a".execute().text
'''.trim()

String result
Jenkins.instance.slaves.find { agent ->
    agent.name == agentName
}.with { agent ->
    result = RemotingDiagnostics.executeGroovy(groovy_script, agent.channel)
}
//println result
def jobName = "My Pipeline"  
def job = Jenkins.instance.getItem(jobName).getItemByBranchName("helloworld")
//println job.metaClass.methods*.name
job.getBuilds().each { 
  println(it.getDisplayName()) 
  println(it.getResult()) 
  if (it.getResult() != Result.SUCCESS) {
    it.delete()
  }
}  
//job.nextBuildNumber = 1   
job.save()
