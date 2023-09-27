#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ComponentId import ComponentId


class TaskQuery(object):

    def __init__(self):
        self._app_keys = None
        self._approve_enabled = None
        self._assignee_work_id = None
        self._body = None
        self._creator_work_id = None
        self._direction = None
        self._from_date = None
        self._group_by_package = None
        self._include_agent_task = None
        self._index_1 = None
        self._index_2 = None
        self._index_3 = None
        self._index_4 = None
        self._is_urge = None
        self._language = None
        self._package_id = None
        self._page_index = None
        self._page_size = None
        self._process_code = None
        self._process_codes = None
        self._source_id = None
        self._source_name = None
        self._source_name_en = None
        self._source_name_en_list = None
        self._source_name_list = None
        self._subject = None
        self._subject_en = None
        self._system_type = None
        self._task_category_uuid = None
        self._task_source_query_infos = None
        self._task_status = None
        self._task_status_list = None
        self._to_date = None

    @property
    def app_keys(self):
        return self._app_keys

    @app_keys.setter
    def app_keys(self, value):
        if isinstance(value, list):
            self._app_keys = list()
            for i in value:
                self._app_keys.append(i)
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
    def creator_work_id(self):
        return self._creator_work_id

    @creator_work_id.setter
    def creator_work_id(self, value):
        self._creator_work_id = value
    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, value):
        self._direction = value
    @property
    def from_date(self):
        return self._from_date

    @from_date.setter
    def from_date(self, value):
        self._from_date = value
    @property
    def group_by_package(self):
        return self._group_by_package

    @group_by_package.setter
    def group_by_package(self, value):
        self._group_by_package = value
    @property
    def include_agent_task(self):
        return self._include_agent_task

    @include_agent_task.setter
    def include_agent_task(self, value):
        self._include_agent_task = value
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
    def is_urge(self):
        return self._is_urge

    @is_urge.setter
    def is_urge(self, value):
        self._is_urge = value
    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, value):
        self._language = value
    @property
    def package_id(self):
        return self._package_id

    @package_id.setter
    def package_id(self, value):
        self._package_id = value
    @property
    def page_index(self):
        return self._page_index

    @page_index.setter
    def page_index(self, value):
        self._page_index = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def process_code(self):
        return self._process_code

    @process_code.setter
    def process_code(self, value):
        self._process_code = value
    @property
    def process_codes(self):
        return self._process_codes

    @process_codes.setter
    def process_codes(self, value):
        if isinstance(value, list):
            self._process_codes = list()
            for i in value:
                self._process_codes.append(i)
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
    def source_name_en_list(self):
        return self._source_name_en_list

    @source_name_en_list.setter
    def source_name_en_list(self, value):
        if isinstance(value, list):
            self._source_name_en_list = list()
            for i in value:
                self._source_name_en_list.append(i)
    @property
    def source_name_list(self):
        return self._source_name_list

    @source_name_list.setter
    def source_name_list(self, value):
        if isinstance(value, list):
            self._source_name_list = list()
            for i in value:
                self._source_name_list.append(i)
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
    def task_category_uuid(self):
        return self._task_category_uuid

    @task_category_uuid.setter
    def task_category_uuid(self, value):
        self._task_category_uuid = value
    @property
    def task_source_query_infos(self):
        return self._task_source_query_infos

    @task_source_query_infos.setter
    def task_source_query_infos(self, value):
        if isinstance(value, list):
            self._task_source_query_infos = list()
            for i in value:
                if isinstance(i, ComponentId):
                    self._task_source_query_infos.append(i)
                else:
                    self._task_source_query_infos.append(ComponentId.from_alipay_dict(i))
    @property
    def task_status(self):
        return self._task_status

    @task_status.setter
    def task_status(self, value):
        self._task_status = value
    @property
    def task_status_list(self):
        return self._task_status_list

    @task_status_list.setter
    def task_status_list(self, value):
        if isinstance(value, list):
            self._task_status_list = list()
            for i in value:
                self._task_status_list.append(i)
    @property
    def to_date(self):
        return self._to_date

    @to_date.setter
    def to_date(self, value):
        self._to_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_keys:
            if isinstance(self.app_keys, list):
                for i in range(0, len(self.app_keys)):
                    element = self.app_keys[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.app_keys[i] = element.to_alipay_dict()
            if hasattr(self.app_keys, 'to_alipay_dict'):
                params['app_keys'] = self.app_keys.to_alipay_dict()
            else:
                params['app_keys'] = self.app_keys
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
        if self.creator_work_id:
            if hasattr(self.creator_work_id, 'to_alipay_dict'):
                params['creator_work_id'] = self.creator_work_id.to_alipay_dict()
            else:
                params['creator_work_id'] = self.creator_work_id
        if self.direction:
            if hasattr(self.direction, 'to_alipay_dict'):
                params['direction'] = self.direction.to_alipay_dict()
            else:
                params['direction'] = self.direction
        if self.from_date:
            if hasattr(self.from_date, 'to_alipay_dict'):
                params['from_date'] = self.from_date.to_alipay_dict()
            else:
                params['from_date'] = self.from_date
        if self.group_by_package:
            if hasattr(self.group_by_package, 'to_alipay_dict'):
                params['group_by_package'] = self.group_by_package.to_alipay_dict()
            else:
                params['group_by_package'] = self.group_by_package
        if self.include_agent_task:
            if hasattr(self.include_agent_task, 'to_alipay_dict'):
                params['include_agent_task'] = self.include_agent_task.to_alipay_dict()
            else:
                params['include_agent_task'] = self.include_agent_task
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
        if self.is_urge:
            if hasattr(self.is_urge, 'to_alipay_dict'):
                params['is_urge'] = self.is_urge.to_alipay_dict()
            else:
                params['is_urge'] = self.is_urge
        if self.language:
            if hasattr(self.language, 'to_alipay_dict'):
                params['language'] = self.language.to_alipay_dict()
            else:
                params['language'] = self.language
        if self.package_id:
            if hasattr(self.package_id, 'to_alipay_dict'):
                params['package_id'] = self.package_id.to_alipay_dict()
            else:
                params['package_id'] = self.package_id
        if self.page_index:
            if hasattr(self.page_index, 'to_alipay_dict'):
                params['page_index'] = self.page_index.to_alipay_dict()
            else:
                params['page_index'] = self.page_index
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.process_code:
            if hasattr(self.process_code, 'to_alipay_dict'):
                params['process_code'] = self.process_code.to_alipay_dict()
            else:
                params['process_code'] = self.process_code
        if self.process_codes:
            if isinstance(self.process_codes, list):
                for i in range(0, len(self.process_codes)):
                    element = self.process_codes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.process_codes[i] = element.to_alipay_dict()
            if hasattr(self.process_codes, 'to_alipay_dict'):
                params['process_codes'] = self.process_codes.to_alipay_dict()
            else:
                params['process_codes'] = self.process_codes
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
        if self.source_name_en_list:
            if isinstance(self.source_name_en_list, list):
                for i in range(0, len(self.source_name_en_list)):
                    element = self.source_name_en_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.source_name_en_list[i] = element.to_alipay_dict()
            if hasattr(self.source_name_en_list, 'to_alipay_dict'):
                params['source_name_en_list'] = self.source_name_en_list.to_alipay_dict()
            else:
                params['source_name_en_list'] = self.source_name_en_list
        if self.source_name_list:
            if isinstance(self.source_name_list, list):
                for i in range(0, len(self.source_name_list)):
                    element = self.source_name_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.source_name_list[i] = element.to_alipay_dict()
            if hasattr(self.source_name_list, 'to_alipay_dict'):
                params['source_name_list'] = self.source_name_list.to_alipay_dict()
            else:
                params['source_name_list'] = self.source_name_list
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
        if self.task_category_uuid:
            if hasattr(self.task_category_uuid, 'to_alipay_dict'):
                params['task_category_uuid'] = self.task_category_uuid.to_alipay_dict()
            else:
                params['task_category_uuid'] = self.task_category_uuid
        if self.task_source_query_infos:
            if isinstance(self.task_source_query_infos, list):
                for i in range(0, len(self.task_source_query_infos)):
                    element = self.task_source_query_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.task_source_query_infos[i] = element.to_alipay_dict()
            if hasattr(self.task_source_query_infos, 'to_alipay_dict'):
                params['task_source_query_infos'] = self.task_source_query_infos.to_alipay_dict()
            else:
                params['task_source_query_infos'] = self.task_source_query_infos
        if self.task_status:
            if hasattr(self.task_status, 'to_alipay_dict'):
                params['task_status'] = self.task_status.to_alipay_dict()
            else:
                params['task_status'] = self.task_status
        if self.task_status_list:
            if isinstance(self.task_status_list, list):
                for i in range(0, len(self.task_status_list)):
                    element = self.task_status_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.task_status_list[i] = element.to_alipay_dict()
            if hasattr(self.task_status_list, 'to_alipay_dict'):
                params['task_status_list'] = self.task_status_list.to_alipay_dict()
            else:
                params['task_status_list'] = self.task_status_list
        if self.to_date:
            if hasattr(self.to_date, 'to_alipay_dict'):
                params['to_date'] = self.to_date.to_alipay_dict()
            else:
                params['to_date'] = self.to_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TaskQuery()
        if 'app_keys' in d:
            o.app_keys = d['app_keys']
        if 'approve_enabled' in d:
            o.approve_enabled = d['approve_enabled']
        if 'assignee_work_id' in d:
            o.assignee_work_id = d['assignee_work_id']
        if 'body' in d:
            o.body = d['body']
        if 'creator_work_id' in d:
            o.creator_work_id = d['creator_work_id']
        if 'direction' in d:
            o.direction = d['direction']
        if 'from_date' in d:
            o.from_date = d['from_date']
        if 'group_by_package' in d:
            o.group_by_package = d['group_by_package']
        if 'include_agent_task' in d:
            o.include_agent_task = d['include_agent_task']
        if 'index_1' in d:
            o.index_1 = d['index_1']
        if 'index_2' in d:
            o.index_2 = d['index_2']
        if 'index_3' in d:
            o.index_3 = d['index_3']
        if 'index_4' in d:
            o.index_4 = d['index_4']
        if 'is_urge' in d:
            o.is_urge = d['is_urge']
        if 'language' in d:
            o.language = d['language']
        if 'package_id' in d:
            o.package_id = d['package_id']
        if 'page_index' in d:
            o.page_index = d['page_index']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'process_code' in d:
            o.process_code = d['process_code']
        if 'process_codes' in d:
            o.process_codes = d['process_codes']
        if 'source_id' in d:
            o.source_id = d['source_id']
        if 'source_name' in d:
            o.source_name = d['source_name']
        if 'source_name_en' in d:
            o.source_name_en = d['source_name_en']
        if 'source_name_en_list' in d:
            o.source_name_en_list = d['source_name_en_list']
        if 'source_name_list' in d:
            o.source_name_list = d['source_name_list']
        if 'subject' in d:
            o.subject = d['subject']
        if 'subject_en' in d:
            o.subject_en = d['subject_en']
        if 'system_type' in d:
            o.system_type = d['system_type']
        if 'task_category_uuid' in d:
            o.task_category_uuid = d['task_category_uuid']
        if 'task_source_query_infos' in d:
            o.task_source_query_infos = d['task_source_query_infos']
        if 'task_status' in d:
            o.task_status = d['task_status']
        if 'task_status_list' in d:
            o.task_status_list = d['task_status_list']
        if 'to_date' in d:
            o.to_date = d['to_date']
        return o


