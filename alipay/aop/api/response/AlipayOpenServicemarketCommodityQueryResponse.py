#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenServicemarketCommodityQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenServicemarketCommodityQueryResponse, self).__init__()
        self._app_hot_logo = None
        self._audit_memo = None
        self._authorization_file = None
        self._biz_type_code = None
        self._category_code = None
        self._category_id = None
        self._commodity_affiliation = None
        self._commodity_id = None
        self._contactor = None
        self._create_date = None
        self._log_url = None
        self._mobile_visiturl = None
        self._name = None
        self._phone = None
        self._status = None
        self._sub_status = None
        self._subtitle = None
        self._test_detail = None
        self._test_report = None
        self._title = None
        self._user_guide = None
        self._user_id = None

    @property
    def app_hot_logo(self):
        return self._app_hot_logo

    @app_hot_logo.setter
    def app_hot_logo(self, value):
        self._app_hot_logo = value
    @property
    def audit_memo(self):
        return self._audit_memo

    @audit_memo.setter
    def audit_memo(self, value):
        self._audit_memo = value
    @property
    def authorization_file(self):
        return self._authorization_file

    @authorization_file.setter
    def authorization_file(self, value):
        self._authorization_file = value
    @property
    def biz_type_code(self):
        return self._biz_type_code

    @biz_type_code.setter
    def biz_type_code(self, value):
        self._biz_type_code = value
    @property
    def category_code(self):
        return self._category_code

    @category_code.setter
    def category_code(self, value):
        self._category_code = value
    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value
    @property
    def commodity_affiliation(self):
        return self._commodity_affiliation

    @commodity_affiliation.setter
    def commodity_affiliation(self, value):
        self._commodity_affiliation = value
    @property
    def commodity_id(self):
        return self._commodity_id

    @commodity_id.setter
    def commodity_id(self, value):
        self._commodity_id = value
    @property
    def contactor(self):
        return self._contactor

    @contactor.setter
    def contactor(self, value):
        self._contactor = value
    @property
    def create_date(self):
        return self._create_date

    @create_date.setter
    def create_date(self, value):
        self._create_date = value
    @property
    def log_url(self):
        return self._log_url

    @log_url.setter
    def log_url(self, value):
        self._log_url = value
    @property
    def mobile_visiturl(self):
        return self._mobile_visiturl

    @mobile_visiturl.setter
    def mobile_visiturl(self, value):
        self._mobile_visiturl = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def sub_status(self):
        return self._sub_status

    @sub_status.setter
    def sub_status(self, value):
        self._sub_status = value
    @property
    def subtitle(self):
        return self._subtitle

    @subtitle.setter
    def subtitle(self, value):
        self._subtitle = value
    @property
    def test_detail(self):
        return self._test_detail

    @test_detail.setter
    def test_detail(self, value):
        self._test_detail = value
    @property
    def test_report(self):
        return self._test_report

    @test_report.setter
    def test_report(self, value):
        self._test_report = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def user_guide(self):
        return self._user_guide

    @user_guide.setter
    def user_guide(self, value):
        self._user_guide = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenServicemarketCommodityQueryResponse, self).parse_response_content(response_content)
        if 'app_hot_logo' in response:
            self.app_hot_logo = response['app_hot_logo']
        if 'audit_memo' in response:
            self.audit_memo = response['audit_memo']
        if 'authorization_file' in response:
            self.authorization_file = response['authorization_file']
        if 'biz_type_code' in response:
            self.biz_type_code = response['biz_type_code']
        if 'category_code' in response:
            self.category_code = response['category_code']
        if 'category_id' in response:
            self.category_id = response['category_id']
        if 'commodity_affiliation' in response:
            self.commodity_affiliation = response['commodity_affiliation']
        if 'commodity_id' in response:
            self.commodity_id = response['commodity_id']
        if 'contactor' in response:
            self.contactor = response['contactor']
        if 'create_date' in response:
            self.create_date = response['create_date']
        if 'log_url' in response:
            self.log_url = response['log_url']
        if 'mobile_visiturl' in response:
            self.mobile_visiturl = response['mobile_visiturl']
        if 'name' in response:
            self.name = response['name']
        if 'phone' in response:
            self.phone = response['phone']
        if 'status' in response:
            self.status = response['status']
        if 'sub_status' in response:
            self.sub_status = response['sub_status']
        if 'subtitle' in response:
            self.subtitle = response['subtitle']
        if 'test_detail' in response:
            self.test_detail = response['test_detail']
        if 'test_report' in response:
            self.test_report = response['test_report']
        if 'title' in response:
            self.title = response['title']
        if 'user_guide' in response:
            self.user_guide = response['user_guide']
        if 'user_id' in response:
            self.user_id = response['user_id']
