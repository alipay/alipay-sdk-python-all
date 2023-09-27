#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ComponentId import ComponentId


class AntTask(object):

    def __init__(self):
        self._activity_id = None
        self._actual_work_id = None
        self._app_key = None
        self._approve_enabled = None
        self._assignee_work_id = None
        self._body = None
        self._component_id = None
        self._create_time = None
        self._creator_work_id = None
        self._dept_id = None
        self._end_time = None
        self._finished_time = None
        self._id = None
        self._index_1 = None
        self._index_2 = None
        self._index_3 = None
        self._index_4 = None
        self._internal_package_id = None
        self._last_update_time = None
        self._main_task_id = None
        self._mobile_url = None
        self._original_work_id = None
        self._overdue_send_next_time = None
        self._overdue_time = None
        self._owner = None
        self._package_id = None
        self._parent_package_id = None
        self._process_code = None
        self._proxy_task_id_list = None
        self._quick_approval = None
        self._real_mobile_url = None
        self._send_card = None
        self._send_count = None
        self._source_id = None
        self._source_name = None
        self._source_name_en = None
        self._start_time = None
        self._subject = None
        self._subject_en = None
        self._system_type = None
        self._task_id = None
        self._task_status = None
        self._task_type = None
        self._top_time = None
        self._urge_num = None
        self._url = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def actual_work_id(self):
        return self._actual_work_id

    @actual_work_id.setter
    def actual_work_id(self, value):
        self._actual_work_id = value
    @property
    def app_key(self):
        return self._app_key

    @app_key.setter
    def app_key(self, value):
        self._app_key = value
    @property
    def approve_enabled(self):
        return self._approve_enabled

    @approve_enabled.setter
    def approve_enabled(self, value):
        self._approve_enabled = value
    @property
    def assignee_work_id(self):
        return self._assignee_work_id

    @assignee_work_id.setter
    def assignee_work_id(self, value):
        self._assignee_work_id = value
    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, value):
        self._body = value
    @property
    def component_id(self):
        return self._component_id

    @component_id.setter
    def component_id(self, value):
        if isinstance(value, ComponentId):
            self._component_id = value
        else:
            self._component_id = ComponentId.from_alipay_dict(value)
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def creator_work_id(self):
        return self._creator_work_id

    @creator_work_id.setter
    def creator_work_id(self, value):
        self._creator_work_id = value
    @property
    def dept_id(self):
        return self._dept_id

    @dept_id.setter
    def dept_id(self, value):
        self._dept_id = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def finished_time(self):
        return self._finished_time

    @finished_time.setter
    def finished_time(self, value):
        self._finished_time = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def index_1(self):
        return self._index_1

    @index_1.setter
    def index_1(self, value):
        self._index_1 = value
    @property
    def index_2(self):
        return self._index_2

    @index_2.setter
    def index_2(self, value):
        self._index_2 = value
    @property
    def index_3(self):
        return self._index_3

    @index_3.setter
    def index_3(self, value):
        self._index_3 = value
    @property
    def index_4(self):
        return self._index_4

    @index_4.setter
    def index_4(self, value):
        self._index_4 = value
    @property
    def internal_package_id(self):
        return self._internal_package_id

    @internal_package_id.setter
    def internal_package_id(self, value):
        self._internal_package_id = value
    @property
    def last_update_time(self):
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, value):
        self._last_update_time = value
    @property
    def main_task_id(self):
        return self._main_task_id

    @main_task_id.setter
    def main_task_id(self, value):
        self._main_task_id = value
    @property
    def mobile_url(self):
        return self._mobile_url

    @mobile_url.setter
    def mobile_url(self, value):
        self._mobile_url = value
    @property
    def original_work_id(self):
        return self._original_work_id

    @original_work_id.setter
    def original_work_id(self, value):
        self._original_work_id = value
    @property
    def overdue_send_next_time(self):
        return self._overdue_send_next_time

    @overdue_send_next_time.setter
    def overdue_send_next_time(self, value):
        self._overdue_send_next_time = value
    @property
    def overdue_time(self):
        return self._overdue_time

    @overdue_time.setter
    def overdue_time(self, value):
        self._overdue_time = value
    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        self._owner = value
    @property
    def package_id(self):
        return self._package_id

    @package_id.setter
    def package_id(self, value):
        self._package_id = value
    @property
    def parent_package_id(self):
        return self._parent_package_id

    @parent_package_id.setter
    def parent_package_id(self, value):
        self._parent_package_id = value
    @property
    def process_code(self):
        return self._process_code

    @process_code.setter
    def process_code(self, value):
        self._process_code = value
    @property
    def proxy_task_id_list(self):
        return self._proxy_task_id_list

    @proxy_task_id_list.setter
    def proxy_task_id_list(self, value):
        if isinstance(value, list):
            self._proxy_task_id_list = list()
            for i in value:
                self._proxy_task_id_list.append(i)
    @property
    def quick_approval(self):
        return self._quick_approval

    @quick_approval.setter
    def quick_approval(self, value):
        self._quick_approval = value
    @property
    def real_mobile_url(self):
        return self._real_mobile_url

    @real_mobile_url.setter
    def real_mobile_url(self, value):
        self._real_mobile_url = value
    @property
    def send_card(self):
        return self._send_card

    @send_card.setter
    def send_card(self, value):
        self._send_card = value
    @property
    def send_count(self):
        return self._send_count

    @send_count.setter
    def send_count(self, value):
        self._send_count = value
    @property
    def source_id(self):
        return self._source_id

    @source_id.setter
    def source_id(self, value):
        self._source_id = value
    @property
    def source_name(self):
        return self._source_name

    @source_name.setter
    def source_name(self, value):
        self._source_name = value
    @property
    def source_name_en(self):
        return self._source_name_en

    @source_name_en.setter
    def source_name_en(self, value):
        self._source_name_en = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value
    @property
    def subject_en(self):
        return self._subject_en

    @subject_en.setter
    def subject_en(self, value):
        self._subject_en = value
    @property
    def system_type(self):
        return self._system_type

    @system_type.setter
    def system_type(self, value):
        self._system_type = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value
    @property
    def task_status(self):
        return self._task_status

    @task_status.setter
    def task_status(self, value):
        self._task_status = value
    @property
    def task_type(self):
        return self._task_type

    @task_type.setter
    def task_type(self, value):
        self._task_type = value
    @property
    def top_time(self):
        return self._top_time

    @top_time.setter
    def top_time(self, value):
        self._top_time = value
    @property
    def urge_num(self):
        return self._urge_num

    @urge_num.setter
    def urge_num(self, value):
        self._urge_num = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.actual_work_id:
            if hasattr(self.actual_work_id, 'to_alipay_dict'):
                params['actual_work_id'] = self.actual_work_id.to_alipay_dict()
            else:
                params['actual_work_id'] = self.actual_work_id
        if self.app_key:
            if hasattr(self.app_key, 'to_alipay_dict'):
                params['app_key'] = self.app_key.to_alipay_dict()
            else:
                params['app_key'] = self.app_key
        if self.approve_enabled:
            if hasattr(self.approve_enabled, 'to_alipay_dict'):
                params['approve_enabled'] = self.approve_enabled.to_alipay_dict()
            else:
                params['approve_enabled'] = self.approve_enabled
        if self.assignee_work_id:
            if hasattr(self.assignee_work_id, 'to_alipay_dict'):
                params['assignee_work_id'] = self.assignee_work_id.to_alipay_dict()
            else:
                params['assignee_work_id'] = self.assignee_work_id
        if self.body:
            if hasattr(self.body, 'to_alipay_dict'):
                params['body'] = self.body.to_alipay_dict()
            else:
                params['body'] = self.body
        if self.component_id:
            if hasattr(self.component_id, 'to_alipay_dict'):
                params['component_id'] = self.component_id.to_alipay_dict()
            else:
                params['component_id'] = self.component_id
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.creator_work_id:
            if hasattr(self.creator_work_id, 'to_alipay_dict'):
                params['creator_work_id'] = self.creator_work_id.to_alipay_dict()
            else:
                params['creator_work_id'] = self.creator_work_id
        if self.dept_id:
            if hasattr(self.dept_id, 'to_alipay_dict'):
                params['dept_id'] = self.dept_id.to_alipay_dict()
            else:
                params['dept_id'] = self.dept_id
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.finished_time:
            if hasattr(self.finished_time, 'to_alipay_dict'):
                params['finished_time'] = self.finished_time.to_alipay_dict()
            else:
                params['finished_time'] = self.finished_time
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.index_1:
            if hasattr(self.index_1, 'to_alipay_dict'):
                params['index_1'] = self.index_1.to_alipay_dict()
            else:
                params['index_1'] = self.index_1
        if self.index_2:
            if hasattr(self.index_2, 'to_alipay_dict'):
                params['index_2'] = self.index_2.to_alipay_dict()
            else:
                params['index_2'] = self.index_2
        if self.index_3:
            if hasattr(self.index_3, 'to_alipay_dict'):
                params['index_3'] = self.index_3.to_alipay_dict()
            else:
                params['index_3'] = self.index_3
        if self.index_4:
            if hasattr(self.index_4, 'to_alipay_dict'):
                params['index_4'] = self.index_4.to_alipay_dict()
            else:
                params['index_4'] = self.index_4
        if self.internal_package_id:
            if hasattr(self.internal_package_id, 'to_alipay_dict'):
                params['internal_package_id'] = self.internal_package_id.to_alipay_dict()
            else:
                params['internal_package_id'] = self.internal_package_id
        if self.last_update_time:
            if hasattr(self.last_update_time, 'to_alipay_dict'):
                params['last_update_time'] = self.last_update_time.to_alipay_dict()
            else:
                params['last_update_time'] = self.last_update_time
        if self.main_task_id:
            if hasattr(self.main_task_id, 'to_alipay_dict'):
                params['main_task_id'] = self.main_task_id.to_alipay_dict()
            else:
                params['main_task_id'] = self.main_task_id
        if self.mobile_url:
            if hasattr(self.mobile_url, 'to_alipay_dict'):
                params['mobile_url'] = self.mobile_url.to_alipay_dict()
            else:
                params['mobile_url'] = self.mobile_url
        if self.original_work_id:
            if hasattr(self.original_work_id, 'to_alipay_dict'):
                params['original_work_id'] = self.original_work_id.to_alipay_dict()
            else:
                params['original_work_id'] = self.original_work_id
        if self.overdue_send_next_time:
            if hasattr(self.overdue_send_next_time, 'to_alipay_dict'):
                params['overdue_send_next_time'] = self.overdue_send_next_time.to_alipay_dict()
            else:
                params['overdue_send_next_time'] = self.overdue_send_next_time
        if self.overdue_time:
            if hasattr(self.overdue_time, 'to_alipay_dict'):
                params['overdue_time'] = self.overdue_time.to_alipay_dict()
            else:
                params['overdue_time'] = self.overdue_time
        if self.owner:
            if hasattr(self.owner, 'to_alipay_dict'):
                params['owner'] = self.owner.to_alipay_dict()
            else:
                params['owner'] = self.owner
        if self.package_id:
            if hasattr(self.package_id, 'to_alipay_dict'):
                params['package_id'] = self.package_id.to_alipay_dict()
            else:
                params['package_id'] = self.package_id
        if self.parent_package_id:
            if hasattr(self.parent_package_id, 'to_alipay_dict'):
                params['parent_package_id'] = self.parent_package_id.to_alipay_dict()
            else:
                params['parent_package_id'] = self.parent_package_id
        if self.process_code:
            if hasattr(self.process_code, 'to_alipay_dict'):
                params['process_code'] = self.process_code.to_alipay_dict()
            else:
                params['process_code'] = self.process_code
        if self.proxy_task_id_list:
            if isinstance(self.proxy_task_id_list, list):
                for i in range(0, len(self.proxy_task_id_list)):
                    element = self.proxy_task_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.proxy_task_id_list[i] = element.to_alipay_dict()
            if hasattr(self.proxy_task_id_list, 'to_alipay_dict'):
                params['proxy_task_id_list'] = self.proxy_task_id_list.to_alipay_dict()
            else:
                params['proxy_task_id_list'] = self.proxy_task_id_list
        if self.quick_approval:
            if hasattr(self.quick_approval, 'to_alipay_dict'):
                params['quick_approval'] = self.quick_approval.to_alipay_dict()
            else:
                params['quick_approval'] = self.quick_approval
        if self.real_mobile_url:
            if hasattr(self.real_mobile_url, 'to_alipay_dict'):
                params['real_mobile_url'] = self.real_mobile_url.to_alipay_dict()
            else:
                params['real_mobile_url'] = self.real_mobile_url
        if self.send_card:
            if hasattr(self.send_card, 'to_alipay_dict'):
                params['send_card'] = self.send_card.to_alipay_dict()
            else:
                params['send_card'] = self.send_card
        if self.send_count:
            if hasattr(self.send_count, 'to_alipay_dict'):
                params['send_count'] = self.send_count.to_alipay_dict()
            else:
                params['send_count'] = self.send_count
        if self.source_id:
            if hasattr(self.source_id, 'to_alipay_dict'):
                params['source_id'] = self.source_id.to_alipay_dict()
            else:
                params['source_id'] = self.source_id
        if self.source_name:
            if hasattr(self.source_name, 'to_alipay_dict'):
                params['source_name'] = self.source_name.to_alipay_dict()
            else:
                params['source_name'] = self.source_name
        if self.source_name_en:
            if hasattr(self.source_name_en, 'to_alipay_dict'):
                params['source_name_en'] = self.source_name_en.to_alipay_dict()
            else:
                params['source_name_en'] = self.source_name_en
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.subject:
            if hasattr(self.subject, 'to_alipay_dict'):
                params['subject'] = self.subject.to_alipay_dict()
            else:
                params['subject'] = self.subject
        if self.subject_en:
            if hasattr(self.subject_en, 'to_alipay_dict'):
                params['subject_en'] = self.subject_en.to_alipay_dict()
            else:
                params['subject_en'] = self.subject_en
        if self.system_type:
            if hasattr(self.system_type, 'to_alipay_dict'):
                params['system_type'] = self.system_type.to_alipay_dict()
            else:
                params['system_type'] = self.system_type
        if self.task_id:
            if hasattr(self.task_id, 'to_alipay_dict'):
                params['task_id'] = self.task_id.to_alipay_dict()
            else:
                params['task_id'] = self.task_id
        if self.task_status:
            if hasattr(self.task_status, 'to_alipay_dict'):
                params['task_status'] = self.task_status.to_alipay_dict()
            else:
                params['task_status'] = self.task_status
        if self.task_type:
            if hasattr(self.task_type, 'to_alipay_dict'):
                params['task_type'] = self.task_type.to_alipay_dict()
            else:
                params['task_type'] = self.task_type
        if self.top_time:
            if hasattr(self.top_time, 'to_alipay_dict'):
                params['top_time'] = self.top_time.to_alipay_dict()
            else:
                params['top_time'] = self.top_time
        if self.urge_num:
            if hasattr(self.urge_num, 'to_alipay_dict'):
                params['urge_num'] = self.urge_num.to_alipay_dict()
            else:
                params['urge_num'] = self.urge_num
        if self.url:
            if hasattr(self.url, 'to_alipay_dict'):
                params['url'] = self.url.to_alipay_dict()
            else:
                params['url'] = self.url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntTask()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'actual_work_id' in d:
            o.actual_work_id = d['actual_work_id']
        if 'app_key' in d:
            o.app_key = d['app_key']
        if 'approve_enabled' in d:
            o.approve_enabled = d['approve_enabled']
        if 'assignee_work_id' in d:
            o.assignee_work_id = d['assignee_work_id']
        if 'body' in d:
            o.body = d['body']
        if 'component_id' in d:
            o.component_id = d['component_id']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'creator_work_id' in d:
            o.creator_work_id = d['creator_work_id']
        if 'dept_id' in d:
            o.dept_id = d['dept_id']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'finished_time' in d:
            o.finished_time = d['finished_time']
        if 'id' in d:
            o.id = d['id']
        if 'index_1' in d:
            o.index_1 = d['index_1']
        if 'index_2' in d:
            o.index_2 = d['index_2']
        if 'index_3' in d:
            o.index_3 = d['index_3']
        if 'index_4' in d:
            o.index_4 = d['index_4']
        if 'internal_package_id' in d:
            o.internal_package_id = d['internal_package_id']
        if 'last_update_time' in d:
            o.last_update_time = d['last_update_time']
        if 'main_task_id' in d:
            o.main_task_id = d['main_task_id']
        if 'mobile_url' in d:
            o.mobile_url = d['mobile_url']
        if 'original_work_id' in d:
            o.original_work_id = d['original_work_id']
        if 'overdue_send_next_time' in d:
            o.overdue_send_next_time = d['overdue_send_next_time']
        if 'overdue_time' in d:
            o.overdue_time = d['overdue_time']
        if 'owner' in d:
            o.owner = d['owner']
        if 'package_id' in d:
            o.package_id = d['package_id']
        if 'parent_package_id' in d:
            o.parent_package_id = d['parent_package_id']
        if 'process_code' in d:
            o.process_code = d['process_code']
        if 'proxy_task_id_list' in d:
            o.proxy_task_id_list = d['proxy_task_id_list']
        if 'quick_approval' in d:
            o.quick_approval = d['quick_approval']
        if 'real_mobile_url' in d:
            o.real_mobile_url = d['real_mobile_url']
        if 'send_card' in d:
            o.send_card = d['send_card']
        if 'send_count' in d:
            o.send_count = d['send_count']
        if 'source_id' in d:
            o.source_id = d['source_id']
        if 'source_name' in d:
            o.source_name = d['source_name']
        if 'source_name_en' in d:
            o.source_name_en = d['source_name_en']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'subject' in d:
            o.subject = d['subject']
        if 'subject_en' in d:
            o.subject_en = d['subject_en']
        if 'system_type' in d:
            o.system_type = d['system_type']
        if 'task_id' in d:
            o.task_id = d['task_id']
        if 'task_status' in d:
            o.task_status = d['task_status']
        if 'task_type' in d:
            o.task_type = d['task_type']
        if 'top_time' in d:
            o.top_time = d['top_time']
        if 'urge_num' in d:
            o.urge_num = d['urge_num']
        if 'url' in d:
            o.url = d['url']
        return o


