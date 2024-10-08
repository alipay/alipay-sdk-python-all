#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DatabaseTable import DatabaseTable


class OcpCloudSqlDumpTaskRes(object):

    def __init__(self):
        self._cloud_instance_arn = None
        self._database_table_info = None
        self._description = None
        self._download_url = None
        self._expire_time = None
        self._file_size = None
        self._id = None
        self._status = None
        self._user_name = None

    @property
    def cloud_instance_arn(self):
        return self._cloud_instance_arn

    @cloud_instance_arn.setter
    def cloud_instance_arn(self, value):
        self._cloud_instance_arn = value
    @property
    def database_table_info(self):
        return self._database_table_info

    @database_table_info.setter
    def database_table_info(self, value):
        if isinstance(value, list):
            self._database_table_info = list()
            for i in value:
                if isinstance(i, DatabaseTable):
                    self._database_table_info.append(i)
                else:
                    self._database_table_info.append(DatabaseTable.from_alipay_dict(i))
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def download_url(self):
        return self._download_url

    @download_url.setter
    def download_url(self, value):
        self._download_url = value
    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def file_size(self):
        return self._file_size

    @file_size.setter
    def file_size(self, value):
        self._file_size = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.cloud_instance_arn:
            if hasattr(self.cloud_instance_arn, 'to_alipay_dict'):
                params['cloud_instance_arn'] = self.cloud_instance_arn.to_alipay_dict()
            else:
                params['cloud_instance_arn'] = self.cloud_instance_arn
        if self.database_table_info:
            if isinstance(self.database_table_info, list):
                for i in range(0, len(self.database_table_info)):
                    element = self.database_table_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.database_table_info[i] = element.to_alipay_dict()
            if hasattr(self.database_table_info, 'to_alipay_dict'):
                params['database_table_info'] = self.database_table_info.to_alipay_dict()
            else:
                params['database_table_info'] = self.database_table_info
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.download_url:
            if hasattr(self.download_url, 'to_alipay_dict'):
                params['download_url'] = self.download_url.to_alipay_dict()
            else:
                params['download_url'] = self.download_url
        if self.expire_time:
            if hasattr(self.expire_time, 'to_alipay_dict'):
                params['expire_time'] = self.expire_time.to_alipay_dict()
            else:
                params['expire_time'] = self.expire_time
        if self.file_size:
            if hasattr(self.file_size, 'to_alipay_dict'):
                params['file_size'] = self.file_size.to_alipay_dict()
            else:
                params['file_size'] = self.file_size
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OcpCloudSqlDumpTaskRes()
        if 'cloud_instance_arn' in d:
            o.cloud_instance_arn = d['cloud_instance_arn']
        if 'database_table_info' in d:
            o.database_table_info = d['database_table_info']
        if 'description' in d:
            o.description = d['description']
        if 'download_url' in d:
            o.download_url = d['download_url']
        if 'expire_time' in d:
            o.expire_time = d['expire_time']
        if 'file_size' in d:
            o.file_size = d['file_size']
        if 'id' in d:
            o.id = d['id']
        if 'status' in d:
            o.status = d['status']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o


