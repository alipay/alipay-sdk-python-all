#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipmcProcessInstanceOpenMqDTO(object):

    def __init__(self):
        self._app_key = None
        self._business_id = None
        self._create_time = None
        self._deleted_flag = None
        self._dynamic_process_flag = None
        self._finish_time = None
        self._id = None
        self._modify_time = None
        self._originator_id = None
        self._originator_job = None
        self._out_result = None
        self._parent_process_instance_id = None
        self._process_code = None
        self._process_id = None
        self._process_instance_id = None
        self._process_instance_status = None
        self._process_version = None
        self._root_parent_process_instance_id = None
        self._super_process_instance_id = None
        self._title = None
        self._title_en = None
        self._url_card_flag = None

    @property
    def app_key(self):
        return self._app_key

    @app_key.setter
    def app_key(self, value):
        self._app_key = value
    @property
    def business_id(self):
        return self._business_id

    @business_id.setter
    def business_id(self, value):
        self._business_id = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def deleted_flag(self):
        return self._deleted_flag

    @deleted_flag.setter
    def deleted_flag(self, value):
        self._deleted_flag = value
    @property
    def dynamic_process_flag(self):
        return self._dynamic_process_flag

    @dynamic_process_flag.setter
    def dynamic_process_flag(self, value):
        self._dynamic_process_flag = value
    @property
    def finish_time(self):
        return self._finish_time

    @finish_time.setter
    def finish_time(self, value):
        self._finish_time = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def modify_time(self):
        return self._modify_time

    @modify_time.setter
    def modify_time(self, value):
        self._modify_time = value
    @property
    def originator_id(self):
        return self._originator_id

    @originator_id.setter
    def originator_id(self, value):
        self._originator_id = value
    @property
    def originator_job(self):
        return self._originator_job

    @originator_job.setter
    def originator_job(self, value):
        self._originator_job = value
    @property
    def out_result(self):
        return self._out_result

    @out_result.setter
    def out_result(self, value):
        self._out_result = value
    @property
    def parent_process_instance_id(self):
        return self._parent_process_instance_id

    @parent_process_instance_id.setter
    def parent_process_instance_id(self, value):
        self._parent_process_instance_id = value
    @property
    def process_code(self):
        return self._process_code

    @process_code.setter
    def process_code(self, value):
        self._process_code = value
    @property
    def process_id(self):
        return self._process_id

    @process_id.setter
    def process_id(self, value):
        self._process_id = value
    @property
    def process_instance_id(self):
        return self._process_instance_id

    @process_instance_id.setter
    def process_instance_id(self, value):
        self._process_instance_id = value
    @property
    def process_instance_status(self):
        return self._process_instance_status

    @process_instance_status.setter
    def process_instance_status(self, value):
        self._process_instance_status = value
    @property
    def process_version(self):
        return self._process_version

    @process_version.setter
    def process_version(self, value):
        self._process_version = value
    @property
    def root_parent_process_instance_id(self):
        return self._root_parent_process_instance_id

    @root_parent_process_instance_id.setter
    def root_parent_process_instance_id(self, value):
        self._root_parent_process_instance_id = value
    @property
    def super_process_instance_id(self):
        return self._super_process_instance_id

    @super_process_instance_id.setter
    def super_process_instance_id(self, value):
        self._super_process_instance_id = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def title_en(self):
        return self._title_en

    @title_en.setter
    def title_en(self, value):
        self._title_en = value
    @property
    def url_card_flag(self):
        return self._url_card_flag

    @url_card_flag.setter
    def url_card_flag(self, value):
        self._url_card_flag = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_key:
            if hasattr(self.app_key, 'to_alipay_dict'):
                params['app_key'] = self.app_key.to_alipay_dict()
            else:
                params['app_key'] = self.app_key
        if self.business_id:
            if hasattr(self.business_id, 'to_alipay_dict'):
                params['business_id'] = self.business_id.to_alipay_dict()
            else:
                params['business_id'] = self.business_id
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.deleted_flag:
            if hasattr(self.deleted_flag, 'to_alipay_dict'):
                params['deleted_flag'] = self.deleted_flag.to_alipay_dict()
            else:
                params['deleted_flag'] = self.deleted_flag
        if self.dynamic_process_flag:
            if hasattr(self.dynamic_process_flag, 'to_alipay_dict'):
                params['dynamic_process_flag'] = self.dynamic_process_flag.to_alipay_dict()
            else:
                params['dynamic_process_flag'] = self.dynamic_process_flag
        if self.finish_time:
            if hasattr(self.finish_time, 'to_alipay_dict'):
                params['finish_time'] = self.finish_time.to_alipay_dict()
            else:
                params['finish_time'] = self.finish_time
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.modify_time:
            if hasattr(self.modify_time, 'to_alipay_dict'):
                params['modify_time'] = self.modify_time.to_alipay_dict()
            else:
                params['modify_time'] = self.modify_time
        if self.originator_id:
            if hasattr(self.originator_id, 'to_alipay_dict'):
                params['originator_id'] = self.originator_id.to_alipay_dict()
            else:
                params['originator_id'] = self.originator_id
        if self.originator_job:
            if hasattr(self.originator_job, 'to_alipay_dict'):
                params['originator_job'] = self.originator_job.to_alipay_dict()
            else:
                params['originator_job'] = self.originator_job
        if self.out_result:
            if hasattr(self.out_result, 'to_alipay_dict'):
                params['out_result'] = self.out_result.to_alipay_dict()
            else:
                params['out_result'] = self.out_result
        if self.parent_process_instance_id:
            if hasattr(self.parent_process_instance_id, 'to_alipay_dict'):
                params['parent_process_instance_id'] = self.parent_process_instance_id.to_alipay_dict()
            else:
                params['parent_process_instance_id'] = self.parent_process_instance_id
        if self.process_code:
            if hasattr(self.process_code, 'to_alipay_dict'):
                params['process_code'] = self.process_code.to_alipay_dict()
            else:
                params['process_code'] = self.process_code
        if self.process_id:
            if hasattr(self.process_id, 'to_alipay_dict'):
                params['process_id'] = self.process_id.to_alipay_dict()
            else:
                params['process_id'] = self.process_id
        if self.process_instance_id:
            if hasattr(self.process_instance_id, 'to_alipay_dict'):
                params['process_instance_id'] = self.process_instance_id.to_alipay_dict()
            else:
                params['process_instance_id'] = self.process_instance_id
        if self.process_instance_status:
            if hasattr(self.process_instance_status, 'to_alipay_dict'):
                params['process_instance_status'] = self.process_instance_status.to_alipay_dict()
            else:
                params['process_instance_status'] = self.process_instance_status
        if self.process_version:
            if hasattr(self.process_version, 'to_alipay_dict'):
                params['process_version'] = self.process_version.to_alipay_dict()
            else:
                params['process_version'] = self.process_version
        if self.root_parent_process_instance_id:
            if hasattr(self.root_parent_process_instance_id, 'to_alipay_dict'):
                params['root_parent_process_instance_id'] = self.root_parent_process_instance_id.to_alipay_dict()
            else:
                params['root_parent_process_instance_id'] = self.root_parent_process_instance_id
        if self.super_process_instance_id:
            if hasattr(self.super_process_instance_id, 'to_alipay_dict'):
                params['super_process_instance_id'] = self.super_process_instance_id.to_alipay_dict()
            else:
                params['super_process_instance_id'] = self.super_process_instance_id
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.title_en:
            if hasattr(self.title_en, 'to_alipay_dict'):
                params['title_en'] = self.title_en.to_alipay_dict()
            else:
                params['title_en'] = self.title_en
        if self.url_card_flag:
            if hasattr(self.url_card_flag, 'to_alipay_dict'):
                params['url_card_flag'] = self.url_card_flag.to_alipay_dict()
            else:
                params['url_card_flag'] = self.url_card_flag
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipmcProcessInstanceOpenMqDTO()
        if 'app_key' in d:
            o.app_key = d['app_key']
        if 'business_id' in d:
            o.business_id = d['business_id']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'deleted_flag' in d:
            o.deleted_flag = d['deleted_flag']
        if 'dynamic_process_flag' in d:
            o.dynamic_process_flag = d['dynamic_process_flag']
        if 'finish_time' in d:
            o.finish_time = d['finish_time']
        if 'id' in d:
            o.id = d['id']
        if 'modify_time' in d:
            o.modify_time = d['modify_time']
        if 'originator_id' in d:
            o.originator_id = d['originator_id']
        if 'originator_job' in d:
            o.originator_job = d['originator_job']
        if 'out_result' in d:
            o.out_result = d['out_result']
        if 'parent_process_instance_id' in d:
            o.parent_process_instance_id = d['parent_process_instance_id']
        if 'process_code' in d:
            o.process_code = d['process_code']
        if 'process_id' in d:
            o.process_id = d['process_id']
        if 'process_instance_id' in d:
            o.process_instance_id = d['process_instance_id']
        if 'process_instance_status' in d:
            o.process_instance_status = d['process_instance_status']
        if 'process_version' in d:
            o.process_version = d['process_version']
        if 'root_parent_process_instance_id' in d:
            o.root_parent_process_instance_id = d['root_parent_process_instance_id']
        if 'super_process_instance_id' in d:
            o.super_process_instance_id = d['super_process_instance_id']
        if 'title' in d:
            o.title = d['title']
        if 'title_en' in d:
            o.title_en = d['title_en']
        if 'url_card_flag' in d:
            o.url_card_flag = d['url_card_flag']
        return o


