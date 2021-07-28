#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RpaCrawlerTaskVO(object):

    def __init__(self):
        self._algo_id = None
        self._biz_goal = None
        self._creative_code_list = None
        self._creative_group_code = None
        self._creative_group_version = None
        self._crowd_id_list = None
        self._deliver_unit_name = None
        self._end_time = None
        self._fatigue = None
        self._plan_id = None
        self._position_code = None
        self._rule_id = None
        self._start_time = None
        self._strategy_id = None
        self._task_id = None
        self._white_list = None

    @property
    def algo_id(self):
        return self._algo_id

    @algo_id.setter
    def algo_id(self, value):
        self._algo_id = value
    @property
    def biz_goal(self):
        return self._biz_goal

    @biz_goal.setter
    def biz_goal(self, value):
        self._biz_goal = value
    @property
    def creative_code_list(self):
        return self._creative_code_list

    @creative_code_list.setter
    def creative_code_list(self, value):
        if isinstance(value, list):
            self._creative_code_list = list()
            for i in value:
                self._creative_code_list.append(i)
    @property
    def creative_group_code(self):
        return self._creative_group_code

    @creative_group_code.setter
    def creative_group_code(self, value):
        self._creative_group_code = value
    @property
    def creative_group_version(self):
        return self._creative_group_version

    @creative_group_version.setter
    def creative_group_version(self, value):
        self._creative_group_version = value
    @property
    def crowd_id_list(self):
        return self._crowd_id_list

    @crowd_id_list.setter
    def crowd_id_list(self, value):
        if isinstance(value, list):
            self._crowd_id_list = list()
            for i in value:
                self._crowd_id_list.append(i)
    @property
    def deliver_unit_name(self):
        return self._deliver_unit_name

    @deliver_unit_name.setter
    def deliver_unit_name(self, value):
        self._deliver_unit_name = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def fatigue(self):
        return self._fatigue

    @fatigue.setter
    def fatigue(self, value):
        self._fatigue = value
    @property
    def plan_id(self):
        return self._plan_id

    @plan_id.setter
    def plan_id(self, value):
        self._plan_id = value
    @property
    def position_code(self):
        return self._position_code

    @position_code.setter
    def position_code(self, value):
        self._position_code = value
    @property
    def rule_id(self):
        return self._rule_id

    @rule_id.setter
    def rule_id(self, value):
        self._rule_id = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def strategy_id(self):
        return self._strategy_id

    @strategy_id.setter
    def strategy_id(self, value):
        self._strategy_id = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value
    @property
    def white_list(self):
        return self._white_list

    @white_list.setter
    def white_list(self, value):
        if isinstance(value, list):
            self._white_list = list()
            for i in value:
                self._white_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.algo_id:
            if hasattr(self.algo_id, 'to_alipay_dict'):
                params['algo_id'] = self.algo_id.to_alipay_dict()
            else:
                params['algo_id'] = self.algo_id
        if self.biz_goal:
            if hasattr(self.biz_goal, 'to_alipay_dict'):
                params['biz_goal'] = self.biz_goal.to_alipay_dict()
            else:
                params['biz_goal'] = self.biz_goal
        if self.creative_code_list:
            if isinstance(self.creative_code_list, list):
                for i in range(0, len(self.creative_code_list)):
                    element = self.creative_code_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.creative_code_list[i] = element.to_alipay_dict()
            if hasattr(self.creative_code_list, 'to_alipay_dict'):
                params['creative_code_list'] = self.creative_code_list.to_alipay_dict()
            else:
                params['creative_code_list'] = self.creative_code_list
        if self.creative_group_code:
            if hasattr(self.creative_group_code, 'to_alipay_dict'):
                params['creative_group_code'] = self.creative_group_code.to_alipay_dict()
            else:
                params['creative_group_code'] = self.creative_group_code
        if self.creative_group_version:
            if hasattr(self.creative_group_version, 'to_alipay_dict'):
                params['creative_group_version'] = self.creative_group_version.to_alipay_dict()
            else:
                params['creative_group_version'] = self.creative_group_version
        if self.crowd_id_list:
            if isinstance(self.crowd_id_list, list):
                for i in range(0, len(self.crowd_id_list)):
                    element = self.crowd_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.crowd_id_list[i] = element.to_alipay_dict()
            if hasattr(self.crowd_id_list, 'to_alipay_dict'):
                params['crowd_id_list'] = self.crowd_id_list.to_alipay_dict()
            else:
                params['crowd_id_list'] = self.crowd_id_list
        if self.deliver_unit_name:
            if hasattr(self.deliver_unit_name, 'to_alipay_dict'):
                params['deliver_unit_name'] = self.deliver_unit_name.to_alipay_dict()
            else:
                params['deliver_unit_name'] = self.deliver_unit_name
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.fatigue:
            if hasattr(self.fatigue, 'to_alipay_dict'):
                params['fatigue'] = self.fatigue.to_alipay_dict()
            else:
                params['fatigue'] = self.fatigue
        if self.plan_id:
            if hasattr(self.plan_id, 'to_alipay_dict'):
                params['plan_id'] = self.plan_id.to_alipay_dict()
            else:
                params['plan_id'] = self.plan_id
        if self.position_code:
            if hasattr(self.position_code, 'to_alipay_dict'):
                params['position_code'] = self.position_code.to_alipay_dict()
            else:
                params['position_code'] = self.position_code
        if self.rule_id:
            if hasattr(self.rule_id, 'to_alipay_dict'):
                params['rule_id'] = self.rule_id.to_alipay_dict()
            else:
                params['rule_id'] = self.rule_id
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.strategy_id:
            if hasattr(self.strategy_id, 'to_alipay_dict'):
                params['strategy_id'] = self.strategy_id.to_alipay_dict()
            else:
                params['strategy_id'] = self.strategy_id
        if self.task_id:
            if hasattr(self.task_id, 'to_alipay_dict'):
                params['task_id'] = self.task_id.to_alipay_dict()
            else:
                params['task_id'] = self.task_id
        if self.white_list:
            if isinstance(self.white_list, list):
                for i in range(0, len(self.white_list)):
                    element = self.white_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.white_list[i] = element.to_alipay_dict()
            if hasattr(self.white_list, 'to_alipay_dict'):
                params['white_list'] = self.white_list.to_alipay_dict()
            else:
                params['white_list'] = self.white_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RpaCrawlerTaskVO()
        if 'algo_id' in d:
            o.algo_id = d['algo_id']
        if 'biz_goal' in d:
            o.biz_goal = d['biz_goal']
        if 'creative_code_list' in d:
            o.creative_code_list = d['creative_code_list']
        if 'creative_group_code' in d:
            o.creative_group_code = d['creative_group_code']
        if 'creative_group_version' in d:
            o.creative_group_version = d['creative_group_version']
        if 'crowd_id_list' in d:
            o.crowd_id_list = d['crowd_id_list']
        if 'deliver_unit_name' in d:
            o.deliver_unit_name = d['deliver_unit_name']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'fatigue' in d:
            o.fatigue = d['fatigue']
        if 'plan_id' in d:
            o.plan_id = d['plan_id']
        if 'position_code' in d:
            o.position_code = d['position_code']
        if 'rule_id' in d:
            o.rule_id = d['rule_id']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'strategy_id' in d:
            o.strategy_id = d['strategy_id']
        if 'task_id' in d:
            o.task_id = d['task_id']
        if 'white_list' in d:
            o.white_list = d['white_list']
        return o


