#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.UserTaskRightsSimpleDto import UserTaskRightsSimpleDto


class UserNodeTaskSimpleDto(object):

    def __init__(self):
        self._biz_info = None
        self._completed_time = None
        self._out_user_task_id = None
        self._sort = None
        self._task_cycle = None
        self._task_cycle_complete_count = None
        self._task_cycle_dynamic_count = None
        self._task_desc = None
        self._task_id = None
        self._task_image_url = None
        self._task_name = None
        self._task_node = None
        self._task_url = None
        self._user_task_id = None
        self._user_task_rights_list = None
        self._user_task_status = None

    @property
    def biz_info(self):
        return self._biz_info

    @biz_info.setter
    def biz_info(self, value):
        self._biz_info = value
    @property
    def completed_time(self):
        return self._completed_time

    @completed_time.setter
    def completed_time(self, value):
        self._completed_time = value
    @property
    def out_user_task_id(self):
        return self._out_user_task_id

    @out_user_task_id.setter
    def out_user_task_id(self, value):
        self._out_user_task_id = value
    @property
    def sort(self):
        return self._sort

    @sort.setter
    def sort(self, value):
        self._sort = value
    @property
    def task_cycle(self):
        return self._task_cycle

    @task_cycle.setter
    def task_cycle(self, value):
        self._task_cycle = value
    @property
    def task_cycle_complete_count(self):
        return self._task_cycle_complete_count

    @task_cycle_complete_count.setter
    def task_cycle_complete_count(self, value):
        self._task_cycle_complete_count = value
    @property
    def task_cycle_dynamic_count(self):
        return self._task_cycle_dynamic_count

    @task_cycle_dynamic_count.setter
    def task_cycle_dynamic_count(self, value):
        self._task_cycle_dynamic_count = value
    @property
    def task_desc(self):
        return self._task_desc

    @task_desc.setter
    def task_desc(self, value):
        self._task_desc = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value
    @property
    def task_image_url(self):
        return self._task_image_url

    @task_image_url.setter
    def task_image_url(self, value):
        self._task_image_url = value
    @property
    def task_name(self):
        return self._task_name

    @task_name.setter
    def task_name(self, value):
        self._task_name = value
    @property
    def task_node(self):
        return self._task_node

    @task_node.setter
    def task_node(self, value):
        self._task_node = value
    @property
    def task_url(self):
        return self._task_url

    @task_url.setter
    def task_url(self, value):
        self._task_url = value
    @property
    def user_task_id(self):
        return self._user_task_id

    @user_task_id.setter
    def user_task_id(self, value):
        self._user_task_id = value
    @property
    def user_task_rights_list(self):
        return self._user_task_rights_list

    @user_task_rights_list.setter
    def user_task_rights_list(self, value):
        if isinstance(value, list):
            self._user_task_rights_list = list()
            for i in value:
                if isinstance(i, UserTaskRightsSimpleDto):
                    self._user_task_rights_list.append(i)
                else:
                    self._user_task_rights_list.append(UserTaskRightsSimpleDto.from_alipay_dict(i))
    @property
    def user_task_status(self):
        return self._user_task_status

    @user_task_status.setter
    def user_task_status(self, value):
        self._user_task_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_info:
            if hasattr(self.biz_info, 'to_alipay_dict'):
                params['biz_info'] = self.biz_info.to_alipay_dict()
            else:
                params['biz_info'] = self.biz_info
        if self.completed_time:
            if hasattr(self.completed_time, 'to_alipay_dict'):
                params['completed_time'] = self.completed_time.to_alipay_dict()
            else:
                params['completed_time'] = self.completed_time
        if self.out_user_task_id:
            if hasattr(self.out_user_task_id, 'to_alipay_dict'):
                params['out_user_task_id'] = self.out_user_task_id.to_alipay_dict()
            else:
                params['out_user_task_id'] = self.out_user_task_id
        if self.sort:
            if hasattr(self.sort, 'to_alipay_dict'):
                params['sort'] = self.sort.to_alipay_dict()
            else:
                params['sort'] = self.sort
        if self.task_cycle:
            if hasattr(self.task_cycle, 'to_alipay_dict'):
                params['task_cycle'] = self.task_cycle.to_alipay_dict()
            else:
                params['task_cycle'] = self.task_cycle
        if self.task_cycle_complete_count:
            if hasattr(self.task_cycle_complete_count, 'to_alipay_dict'):
                params['task_cycle_complete_count'] = self.task_cycle_complete_count.to_alipay_dict()
            else:
                params['task_cycle_complete_count'] = self.task_cycle_complete_count
        if self.task_cycle_dynamic_count:
            if hasattr(self.task_cycle_dynamic_count, 'to_alipay_dict'):
                params['task_cycle_dynamic_count'] = self.task_cycle_dynamic_count.to_alipay_dict()
            else:
                params['task_cycle_dynamic_count'] = self.task_cycle_dynamic_count
        if self.task_desc:
            if hasattr(self.task_desc, 'to_alipay_dict'):
                params['task_desc'] = self.task_desc.to_alipay_dict()
            else:
                params['task_desc'] = self.task_desc
        if self.task_id:
            if hasattr(self.task_id, 'to_alipay_dict'):
                params['task_id'] = self.task_id.to_alipay_dict()
            else:
                params['task_id'] = self.task_id
        if self.task_image_url:
            if hasattr(self.task_image_url, 'to_alipay_dict'):
                params['task_image_url'] = self.task_image_url.to_alipay_dict()
            else:
                params['task_image_url'] = self.task_image_url
        if self.task_name:
            if hasattr(self.task_name, 'to_alipay_dict'):
                params['task_name'] = self.task_name.to_alipay_dict()
            else:
                params['task_name'] = self.task_name
        if self.task_node:
            if hasattr(self.task_node, 'to_alipay_dict'):
                params['task_node'] = self.task_node.to_alipay_dict()
            else:
                params['task_node'] = self.task_node
        if self.task_url:
            if hasattr(self.task_url, 'to_alipay_dict'):
                params['task_url'] = self.task_url.to_alipay_dict()
            else:
                params['task_url'] = self.task_url
        if self.user_task_id:
            if hasattr(self.user_task_id, 'to_alipay_dict'):
                params['user_task_id'] = self.user_task_id.to_alipay_dict()
            else:
                params['user_task_id'] = self.user_task_id
        if self.user_task_rights_list:
            if isinstance(self.user_task_rights_list, list):
                for i in range(0, len(self.user_task_rights_list)):
                    element = self.user_task_rights_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.user_task_rights_list[i] = element.to_alipay_dict()
            if hasattr(self.user_task_rights_list, 'to_alipay_dict'):
                params['user_task_rights_list'] = self.user_task_rights_list.to_alipay_dict()
            else:
                params['user_task_rights_list'] = self.user_task_rights_list
        if self.user_task_status:
            if hasattr(self.user_task_status, 'to_alipay_dict'):
                params['user_task_status'] = self.user_task_status.to_alipay_dict()
            else:
                params['user_task_status'] = self.user_task_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UserNodeTaskSimpleDto()
        if 'biz_info' in d:
            o.biz_info = d['biz_info']
        if 'completed_time' in d:
            o.completed_time = d['completed_time']
        if 'out_user_task_id' in d:
            o.out_user_task_id = d['out_user_task_id']
        if 'sort' in d:
            o.sort = d['sort']
        if 'task_cycle' in d:
            o.task_cycle = d['task_cycle']
        if 'task_cycle_complete_count' in d:
            o.task_cycle_complete_count = d['task_cycle_complete_count']
        if 'task_cycle_dynamic_count' in d:
            o.task_cycle_dynamic_count = d['task_cycle_dynamic_count']
        if 'task_desc' in d:
            o.task_desc = d['task_desc']
        if 'task_id' in d:
            o.task_id = d['task_id']
        if 'task_image_url' in d:
            o.task_image_url = d['task_image_url']
        if 'task_name' in d:
            o.task_name = d['task_name']
        if 'task_node' in d:
            o.task_node = d['task_node']
        if 'task_url' in d:
            o.task_url = d['task_url']
        if 'user_task_id' in d:
            o.user_task_id = d['user_task_id']
        if 'user_task_rights_list' in d:
            o.user_task_rights_list = d['user_task_rights_list']
        if 'user_task_status' in d:
            o.user_task_status = d['user_task_status']
        return o


