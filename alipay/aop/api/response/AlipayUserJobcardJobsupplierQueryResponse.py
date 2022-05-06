#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.JobInfo import JobInfo


class AlipayUserJobcardJobsupplierQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserJobcardJobsupplierQueryResponse, self).__init__()
        self._basic_info = None
        self._bonus_desc = None
        self._industry_name = None
        self._introduction = None
        self._job_info_list = None
        self._job_supplier_code = None
        self._location_info = None
        self._name = None
        self._page_info = None
        self._status = None
        self._type = None
        self._zhima_cert = None
        self._zhima_cert_url = None

    @property
    def basic_info(self):
        return self._basic_info

    @basic_info.setter
    def basic_info(self, value):
        self._basic_info = value
    @property
    def bonus_desc(self):
        return self._bonus_desc

    @bonus_desc.setter
    def bonus_desc(self, value):
        self._bonus_desc = value
    @property
    def industry_name(self):
        return self._industry_name

    @industry_name.setter
    def industry_name(self, value):
        self._industry_name = value
    @property
    def introduction(self):
        return self._introduction

    @introduction.setter
    def introduction(self, value):
        self._introduction = value
    @property
    def job_info_list(self):
        return self._job_info_list

    @job_info_list.setter
    def job_info_list(self, value):
        if isinstance(value, list):
            self._job_info_list = list()
            for i in value:
                if isinstance(i, JobInfo):
                    self._job_info_list.append(i)
                else:
                    self._job_info_list.append(JobInfo.from_alipay_dict(i))
    @property
    def job_supplier_code(self):
        return self._job_supplier_code

    @job_supplier_code.setter
    def job_supplier_code(self, value):
        self._job_supplier_code = value
    @property
    def location_info(self):
        return self._location_info

    @location_info.setter
    def location_info(self, value):
        self._location_info = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def page_info(self):
        return self._page_info

    @page_info.setter
    def page_info(self, value):
        self._page_info = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def zhima_cert(self):
        return self._zhima_cert

    @zhima_cert.setter
    def zhima_cert(self, value):
        self._zhima_cert = value
    @property
    def zhima_cert_url(self):
        return self._zhima_cert_url

    @zhima_cert_url.setter
    def zhima_cert_url(self, value):
        self._zhima_cert_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserJobcardJobsupplierQueryResponse, self).parse_response_content(response_content)
        if 'basic_info' in response:
            self.basic_info = response['basic_info']
        if 'bonus_desc' in response:
            self.bonus_desc = response['bonus_desc']
        if 'industry_name' in response:
            self.industry_name = response['industry_name']
        if 'introduction' in response:
            self.introduction = response['introduction']
        if 'job_info_list' in response:
            self.job_info_list = response['job_info_list']
        if 'job_supplier_code' in response:
            self.job_supplier_code = response['job_supplier_code']
        if 'location_info' in response:
            self.location_info = response['location_info']
        if 'name' in response:
            self.name = response['name']
        if 'page_info' in response:
            self.page_info = response['page_info']
        if 'status' in response:
            self.status = response['status']
        if 'type' in response:
            self.type = response['type']
        if 'zhima_cert' in response:
            self.zhima_cert = response['zhima_cert']
        if 'zhima_cert_url' in response:
            self.zhima_cert_url = response['zhima_cert_url']
