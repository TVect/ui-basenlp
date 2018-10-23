## Milestones

### Single-Turn QA
- Ontology Construction

dialogue act: 

	inform, request, confirm (system only)
	
	Task-specific action (e.g. book_ticket)

	Others (e.g. thanks)

- Language Understanding

### Multi-Turn Interaction
- User Simulation
- Basic DM

### Learning-Based Agent
- Speech / Multimodal API
- RL-Based DM
- NN-Based NLG

## TODO

- 一句话中出现了多个意图或者提供了一个slot的多个值怎么表示?

eg.1 我想看杭州和上海的天气. request_weather {"city": "杭州", "city": "上海"} 

eg.2 我想看杭州和上海的. inform {"city": "杭州", "city": "上海"} 

eg.3 我想看杭州到上海的列车还有上海的天气. ??????

eg.4 我想看餐馆的电话号码和地址. request [phone_num, address]
