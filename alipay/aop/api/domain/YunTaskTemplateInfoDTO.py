#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PlanInfo import PlanInfo


class YunTaskTemplateInfoDTO(object):

    def __init__(self):
        self._applet_id = None
        self._creator_uid = None
        self._funder_id = None
        self._funder_type = None
        self._gmt_create = None
        self._incentive = None
        self._incentive_mode = None
        self._incentive_rule = None
        self._organizer_id = None
        self._organizer_name = None
        self._organizer_type = None
        self._owner_pid = None
        self._plan_info = None
        self._status = None
        self._task_desc = None
        self._task_end_time = None
        self._task_name = None
        self._task_start_time = None
        self._task_template_id = None
        self._task_type = None

    @property
    def applet_id(self):
        return self._applet_id

    @applet_id.setter
    def applet_id(self, value):
        self._applet_id = value
    @property
    def creator_uid(self):
        return self._creator_uid

    @creator_uid.setter
    def creator_uid(self, value):
        self._creator_uid = value
    @property
    def funder_id(self):
        return self._funder_id

    @funder_id.setter
    def funder_id(self, value):
        self._funder_id = value
    @property
    def funder_type(self):
        return self._funder_type

    @funder_type.setter
    def funder_type(self, value):
        self._funder_type = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def incentive(self):
        return self._incentive

    @incentive.setter
    def incentive(self, value):
        self._incentive = value
    @property
    def incentive_mode(self):
        return self._incentive_mode

    @incentive_mode.setter
    def incentive_mode(self, value):
        self._incentive_mode = value
    @property
    def incentive_rule(self):
        return self._incentive_rule

    @incentive_rule.setter
    def incentive_rule(self, value):
        self._incentive_rule = value
    @property
    def organizer_id(self):
        return self._organizer_id

    @organizer_id.setter
    def organizer_id(self, value):
        self._organizer_id = value
    @property
    def organizer_name(self):
        return self._organizer_name

    @organizer_name.setter
    def organizer_name(self, value):
        self._organizer_name = value
    @property
    def organizer_type(self):
        return self._organizer_type

    @organizer_type.setter
    def organizer_type(self, value):
        self._organizer_type = value
    @property
    def owner_pid(self):
        return self._owner_pid

    @owner_pid.setter
    def owner_pid(self, value):
        self._owner_pid = value
    @property
    def plan_info(self):
        return self._plan_info

    @plan_info.setter
    def plan_info(self, value):
        if isinstance(value, PlanInfo):
            self._plan_info = value
        else:
            self._plan_info = PlanInfo.from_alipay_dict(value)
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def task_desc(self):
        return self._task_desc

    @task_desc.setter
    def task_desc(self, value):
        self._task_desc = value
    @property
    def task_end_time(self):
        return self._task_end_time

    @task_end_time.setter
    def task_end_time(self, value):
        self._task_end_time = value
    @property
    def task_name(self):
        return self._task_name

    @task_name.setter
    def task_name(self, value):
        self._task_name = value
    @property
    def task_start_time(self):
        return self._task_start_time

    @task_start_time.setter
    def task_start_time(self, value):
        self._task_start_time = value
    @property
    def task_template_id(self):
        return self._task_template_id

    @task_template_id.setter
    def task_template_id(self, value):
        self._task_template_id = value
    @property
    def task_type(self):
        return self._task_type

    @task_type.setter
    def task_type(self, value):
        self._task_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.applet_id:
            if hasattr(self.applet_id, 'to_alipay_dict'):
                params['applet_id'] = self.applet_id.to_alipay_dict()
            else:
                params['applet_id'] = self.applet_id
        if self.creator_uid:
            if hasattr(self.creator_uid, 'to_alipay_dict'):
                params['creator_uid'] = self.creator_uid.to_alipay_dict()
            else:
                params['creator_uid'] = self.creator_uid
        if self.funder_id:
            if hasattr(self.funder_id, 'to_alipay_dict'):
                params['funder_id'] = self.funder_id.to_alipay_dict()
            else:
                params['funder_id'] = self.funder_id
        if self.funder_type:
            if hasattr(self.funder_type, 'to_alipay_dict'):
                params['funder_type'] = self.funder_type.to_alipay_dict()
            else:
                params['funder_type'] = self.funder_type
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.incentive:
            if hasattr(self.incentive, 'to_alipay_dict'):
                params['incentive'] = self.incentive.to_alipay_dict()
            else:
                params['incentive'] = self.incentive
        if self.incentive_mode:
            if hasattr(self.incentive_mode, 'to_alipay_dict'):
                params['incentive_mode'] = self.incentive_mode.to_alipay_dict()
            else:
                params['incentive_mode'] = self.incentive_mode
        if self.incentive_rule:
            if hasattr(self.incentive_rule, 'to_alipay_dict'):
                params['incentive_rule'] = self.incentive_rule.to_alipay_dict()
            else:
                params['incentive_rule'] = self.incentive_rule
        if self.organizer_id:
            if hasattr(self.organizer_id, 'to_alipay_dict'):
                params['organizer_id'] = self.organizer_id.to_alipay_dict()
            else:
                params['organizer_id'] = self.organizer_id
        if self.organizer_name:
            if hasattr(self.organizer_name, 'to_alipay_dict'):
                params['organizer_name'] = self.organizer_name.to_alipay_dict()
            else:
                params['organizer_name'] = self.organizer_name
        if self.organizer_type:
            if hasattr(self.organizer_type, 'to_alipay_dict'):
                params['organizer_type'] = self.organizer_type.to_alipay_dict()
            else:
                params['organizer_type'] = self.organizer_type
        if self.owner_pid:
            if hasattr(self.owner_pid, 'to_alipay_dict'):
                params['owner_pid'] = self.owner_pid.to_alipay_dict()
            else:
                params['owner_pid'] = self.owner_pid
        if self.plan_info:
            if hasattr(self.plan_info, 'to_alipay_dict'):
                params['plan_info'] = self.plan_info.to_alipay_dict()
            else:
                params['plan_info'] = self.plan_info
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.task_desc:
            if hasattr(self.task_desc, 'to_alipay_dict'):
                params['task_desc'] = self.task_desc.to_alipay_dict()
            else:
                params['task_desc'] = self.task_desc
        if self.task_end_time:
            if hasattr(self.task_end_time, 'to_alipay_dict'):
                params['task_end_time'] = self.task_end_time.to_alipay_dict()
            else:
                params['task_end_time'] = self.task_end_time
        if self.task_name:
            if hasattr(self.task_name, 'to_alipay_dict'):
                params['task_name'] = self.task_name.to_alipay_dict()
            else:
                params['task_name'] = self.task_name
        if self.task_start_time:
            if hasattr(self.task_start_time, 'to_alipay_dict'):
                params['task_start_time'] = self.task_start_time.to_alipay_dict()
            else:
                params['task_start_time'] = self.task_start_time
        if self.task_template_id:
            if hasattr(self.task_template_id, 'to_alipay_dict'):
                params['task_template_id'] = self.task_template_id.to_alipay_dict()
            else:
                params['task_template_id'] = self.task_template_id
        if self.task_type:
            if hasattr(self.task_type, 'to_alipay_dict'):
                params['task_type'] = self.task_type.to_alipay_dict()
            else:
                params['task_type'] = self.task_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = YunTaskTemplateInfoDTO()
        if 'applet_id' in d:
            o.applet_id = d['applet_id']
        if 'creator_uid' in d:
            o.creator_uid = d['creator_uid']
        if 'funder_id' in d:
            o.funder_id = d['funder_id']
        if 'funder_type' in d:
            o.funder_type = d['funder_type']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'incentive' in d:
            o.incentive = d['incentive']
        if 'incentive_mode' in d:
            o.incentive_mode = d['incentive_mode']
        if 'incentive_rule' in d:
            o.incentive_rule = d['incentive_rule']
        if 'organizer_id' in d:
            o.organizer_id = d['organizer_id']
        if 'organizer_name' in d:
            o.organizer_name = d['organizer_name']
        if 'organizer_type' in d:
            o.organizer_type = d['organizer_type']
        if 'owner_pid' in d:
            o.owner_pid = d['owner_pid']
        if 'plan_info' in d:
            o.plan_info = d['plan_info']
        if 'status' in d:
            o.status = d['status']
        if 'task_desc' in d:
            o.task_desc = d['task_desc']
        if 'task_end_time' in d:
            o.task_end_time = d['task_end_time']
        if 'task_name' in d:
            o.task_name = d['task_name']
        if 'task_start_time' in d:
            o.task_start_time = d['task_start_time']
        if 'task_template_id' in d:
            o.task_template_id = d['task_template_id']
        if 'task_type' in d:
            o.task_type = d['task_type']
        return o


