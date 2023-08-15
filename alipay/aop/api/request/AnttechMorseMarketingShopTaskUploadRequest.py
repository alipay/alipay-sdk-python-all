#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.FileItem import FileItem
from alipay.aop.api.constant.ParamConstants import *

from alipay.aop.api.domain.CategoryRangeInfo import CategoryRangeInfo
from alipay.aop.api.domain.ShopIndustryInfo import ShopIndustryInfo



class AnttechMorseMarketingShopTaskUploadRequest(object):

    def __init__(self, biz_model=None):
        self._biz_model = biz_model
        self._bussiness_code = None
        self._category = None
        self._category_range = None
        self._schedule_time = None
        self._schedule_type = None
        self._shop_industry = None
        self._task_name = None
        self._task_type = None
        self._file_content = None
        self._version = "1.0"
        self._terminal_type = None
        self._terminal_info = None
        self._prod_code = None
        self._notify_url = None
        self._return_url = None
        self._udf_params = None
        self._need_encrypt = False

    @property
    def biz_model(self):
        return self._biz_model

    @biz_model.setter
    def biz_model(self, value):
        self._biz_model = value

    @property
    def bussiness_code(self):
        return self._bussiness_code

    @bussiness_code.setter
    def bussiness_code(self, value):
        self._bussiness_code = value
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, list):
            self._category = list()
            for i in value:
                self._category.append(i)
    @property
    def category_range(self):
        return self._category_range

    @category_range.setter
    def category_range(self, value):
        if isinstance(value, list):
            self._category_range = list()
            for i in value:
                if isinstance(i, CategoryRangeInfo):
                    self._category_range.append(i)
                else:
                    self._category_range.append(CategoryRangeInfo.from_alipay_dict(i))
    @property
    def schedule_time(self):
        return self._schedule_time

    @schedule_time.setter
    def schedule_time(self, value):
        self._schedule_time = value
    @property
    def schedule_type(self):
        return self._schedule_type

    @schedule_type.setter
    def schedule_type(self, value):
        self._schedule_type = value
    @property
    def shop_industry(self):
        return self._shop_industry

    @shop_industry.setter
    def shop_industry(self, value):
        if isinstance(value, list):
            self._shop_industry = list()
            for i in value:
                if isinstance(i, ShopIndustryInfo):
                    self._shop_industry.append(i)
                else:
                    self._shop_industry.append(ShopIndustryInfo.from_alipay_dict(i))
    @property
    def task_name(self):
        return self._task_name

    @task_name.setter
    def task_name(self, value):
        self._task_name = value
    @property
    def task_type(self):
        return self._task_type

    @task_type.setter
    def task_type(self, value):
        self._task_type = value

    @property
    def file_content(self):
        return self._file_content

    @file_content.setter
    def file_content(self, value):
        if not isinstance(value, FileItem):
            return
        self._file_content = value

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, value):
        self._version = value

    @property
    def terminal_type(self):
        return self._terminal_type

    @terminal_type.setter
    def terminal_type(self, value):
        self._terminal_type = value

    @property
    def terminal_info(self):
        return self._terminal_info

    @terminal_info.setter
    def terminal_info(self, value):
        self._terminal_info = value

    @property
    def prod_code(self):
        return self._prod_code

    @prod_code.setter
    def prod_code(self, value):
        self._prod_code = value

    @property
    def notify_url(self):
        return self._notify_url

    @notify_url.setter
    def notify_url(self, value):
        self._notify_url = value

    @property
    def return_url(self):
        return self._return_url

    @return_url.setter
    def return_url(self, value):
        self._return_url = value

    @property
    def udf_params(self):
        return self._udf_params

    @udf_params.setter
    def udf_params(self, value):
        if not isinstance(value, dict):
            return
        self._udf_params = value

    @property
    def need_encrypt(self):
        return self._need_encrypt

    @need_encrypt.setter
    def need_encrypt(self, value):
        self._need_encrypt = value

    def add_other_text_param(self, key, value):
        if not self.udf_params:
            self.udf_params = dict()
        self.udf_params[key] = value

    def get_params(self):
        params = dict()
        params[P_METHOD] = 'anttech.morse.marketing.shop.task.upload'
        params[P_VERSION] = self.version
        if self.biz_model:
            params[P_BIZ_CONTENT] = json.dumps(obj=self.biz_model.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        if self.bussiness_code:
            if hasattr(self.bussiness_code, 'to_alipay_dict'):
                params['bussiness_code'] = json.dumps(obj=self.bussiness_code.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['bussiness_code'] = self.bussiness_code
        if self.category:
            if isinstance(self.category, list):
                for i in range(0, len(self.category)):
                    element = self.category[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.category[i] = element.to_alipay_dict()
                params['category'] = json.dumps(obj=self.category, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        if self.category_range:
            if isinstance(self.category_range, list):
                for i in range(0, len(self.category_range)):
                    element = self.category_range[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.category_range[i] = element.to_alipay_dict()
                params['category_range'] = json.dumps(obj=self.category_range, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        if self.schedule_time:
            if hasattr(self.schedule_time, 'to_alipay_dict'):
                params['schedule_time'] = json.dumps(obj=self.schedule_time.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['schedule_time'] = self.schedule_time
        if self.schedule_type:
            if hasattr(self.schedule_type, 'to_alipay_dict'):
                params['schedule_type'] = json.dumps(obj=self.schedule_type.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['schedule_type'] = self.schedule_type
        if self.shop_industry:
            if isinstance(self.shop_industry, list):
                for i in range(0, len(self.shop_industry)):
                    element = self.shop_industry[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.shop_industry[i] = element.to_alipay_dict()
                params['shop_industry'] = json.dumps(obj=self.shop_industry, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        if self.task_name:
            if hasattr(self.task_name, 'to_alipay_dict'):
                params['task_name'] = json.dumps(obj=self.task_name.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['task_name'] = self.task_name
        if self.task_type:
            if hasattr(self.task_type, 'to_alipay_dict'):
                params['task_type'] = json.dumps(obj=self.task_type.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['task_type'] = self.task_type
        if self.terminal_type:
            params['terminal_type'] = self.terminal_type
        if self.terminal_info:
            params['terminal_info'] = self.terminal_info
        if self.prod_code:
            params['prod_code'] = self.prod_code
        if self.notify_url:
            params['notify_url'] = self.notify_url
        if self.return_url:
            params['return_url'] = self.return_url
        if self.udf_params:
            params.update(self.udf_params)
        return params

    def get_multipart_params(self):
        multipart_params = dict()
        if self.file_content:
            multipart_params['file_content'] = self.file_content
        return multipart_params
