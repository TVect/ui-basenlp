import random
import datetime
from unittest import mock

class MockDoctor:
    
    def _get_random_name(self):
        names = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许',
'何', '吕', '施', '张', '孔', '曹', '严', '华', '金', '魏', '陶', '姜', '戚', '谢', '邹', '喻', '柏', '水', '窦', '章',
'云', '苏', '潘', '葛', '奚', '范', '彭', '郎', '鲁', '韦', '昌', '马', '苗', '凤', '花', '方', '俞', '任', '袁', '柳',
'酆', '鲍', '史', '唐', '费', '廉', '岑', '薛', '雷', '贺', '倪', '汤', '滕', '殷', '罗', '毕', '郝', '邬', '安', '常',
'乐', '于', '时', '傅', '皮', '卞', '齐', '康', '伍', '余', '元', '卜', '顾', '孟', '平', '黄', '和', '穆', '萧', '尹',
'姚', '邵', '堪', '汪', '祁', '毛', '禹', '狄', '米', '贝', '明', '臧', '计', '伏', '成', '戴', '谈', '宋', '茅', '庞',
'熊', '纪', '舒', '屈', '项', '祝', '董', '梁']
        return random.choice(names)+"医生"


    def get_available_doctors(self, **kwargs):
        '''
        @param time: 
        @param department:
        '''
        results = [{"doctorname": self._get_random_name(), 
                    "time": kwargs["time"], 
                    "department": kwargs["department"]},
                   {"doctorname": self._get_random_name(), 
                    "time": kwargs["time"], 
                    "department": kwargs["department"]},
                   {"doctorname": self._get_random_name(), 
                    "time": kwargs["time"], 
                    "department": kwargs["department"]}]
        return {"flag": True, "results": results}


    def get_available_time(self, **kwargs):
        '''
        @param doctorname:
        @param department:
        '''
        day = datetime.date.today()
        results = []
        for _ in range(3):
            day = day + datetime.timedelta(days=random.choice([1,2,3]))
            day_period = day.strftime("%Y-%m-%d")
            results.append({"doctorname": kwargs["doctorname"], 
                            "time": day_period+" 上午" if random.random()>0.5 else day_period+" 下午", 
                            "department": kwargs["department"]})
        
        return {"flag": True, "results": results}


if __name__ == '__main__':
    doctor = MockDoctor()    
    print(doctor.get_available_doctors(time="2018-10-10 上午", department="皮肤科"))
    print(doctor.get_available_time(doctorname="徐医生", department="皮肤科"))