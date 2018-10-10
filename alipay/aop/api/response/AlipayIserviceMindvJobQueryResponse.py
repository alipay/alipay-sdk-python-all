#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayIserviceMindvJobQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceMindvJobQueryResponse, self).__init__()
        self._gmt_create = None
        self._id = None
        self._job_domain = None
        self._name = None
        self._status = None

    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def job_domain(self):
        return self._job_domain

    @job_domain.setter
    def job_domain(self, value):
        self._job_domain = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceMindvJobQueryResponse, self).parse_response_content(response_content)
        if 'gmt_create' in response:
            self.gmt_create = response['gmt_create']
        if 'id' in response:
            self.id = response['id']
        if 'job_domain' in response:
            self.job_domain = response['job_domain']
        if 'name' in response:
            self.name = response['name']
        if 'status' in response:
            self.status = response['status']
