# CrewAI-Agents-Demo

### Creating a single agent and multi-agent

conda create -n agentdemo python=3.11 -y

conda activate agentdemo

pip install -r requirements.txt


#### Research agent
- Take topic from the user and will do research operation over the internet and give you response on top of this.

#### Tool
- SerpAPI: search tool
- https://serper.dev/

# Blog-post generation agent (multi agent)
User will pass one topic name. The research agent will try to do the research operation on the topic. Let's say user agent will do the research operation on the topic. It will give the entire research topic to the next agent. The next agent will try to write that block in the md (mark down) file. It can also be done in json file and text file. 

Trying to make a connection. First agent will research the topic and sent to the second agent to write the blog.