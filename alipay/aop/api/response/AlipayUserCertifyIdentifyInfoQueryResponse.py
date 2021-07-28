#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserCertifyIdentifyInfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserCertifyIdentifyInfoQueryResponse, self).__init__()
        self._cert_name = None
        self._cert_no = None
        self._cert_type = None
        self._certify_grade = None
        self._certify_time = None
        self._havana_id = None
        self._is_certified = None
        self._is_released = None
        self._logon_id = None
        self._org_customer_expire_date = None
        self._org_customer_is_cancelled = None
        self._org_customer_is_exception = None
        self._org_customer_is_in_black_list = None
        self._org_customer_is_revoked = None
        self._org_customer_issue_date = None
        self._org_customer_legal_person_cert_name = None
        self._org_customer_legal_person_cert_no = None
        self._org_customer_legal_person_cert_type = None
        self._org_customer_legal_person_expire_date = None
        self._org_customer_legal_person_pictures = None
        self._org_customer_nature = None
        self._org_customer_open_date = None
        self._org_customer_pictures = None
        self._org_customer_registered_capital = None
        self._org_customer_scope = None
        self._person_customer_expire_date = None
        self._person_customer_pictures = None
        self._person_user_expire_date = None
        self._person_user_pictures = None
        self._user_id = None
        self._user_type = None

    @property
    def cert_name(self):
        return self._cert_name

    @cert_name.setter
    def cert_name(self, value):
        self._cert_name = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def certify_grade(self):
        return self._certify_grade

    @certify_grade.setter
    def certify_grade(self, value):
        self._certify_grade = value
    @property
    def certify_time(self):
        return self._certify_time

    @certify_time.setter
    def certify_time(self, value):
        self._certify_time = value
    @property
    def havana_id(self):
        return self._havana_id

    @havana_id.setter
    def havana_id(self, value):
        self._havana_id = value
    @property
    def is_certified(self):
        return self._is_certified

    @is_certified.setter
    def is_certified(self, value):
        self._is_certified = value
    @property
    def is_released(self):
        return self._is_released

    @is_released.setter
    def is_released(self, value):
        self._is_released = value
    @property
    def logon_id(self):
        return self._logon_id

    @logon_id.setter
    def logon_id(self, value):
        self._logon_id = value
    @property
    def org_customer_expire_date(self):
        return self._org_customer_expire_date

    @org_customer_expire_date.setter
    def org_customer_expire_date(self, value):
        self._org_customer_expire_date = value
    @property
    def org_customer_is_cancelled(self):
        return self._org_customer_is_cancelled

    @org_customer_is_cancelled.setter
    def org_customer_is_cancelled(self, value):
        self._org_customer_is_cancelled = value
    @property
    def org_customer_is_exception(self):
        return self._org_customer_is_exception

    @org_customer_is_exception.setter
    def org_customer_is_exception(self, value):
        self._org_customer_is_exception = value
    @property
    def org_customer_is_in_black_list(self):
        return self._org_customer_is_in_black_list

    @org_customer_is_in_black_list.setter
    def org_customer_is_in_black_list(self, value):
        self._org_customer_is_in_black_list = value
    @property
    def org_customer_is_revoked(self):
        return self._org_customer_is_revoked

    @org_customer_is_revoked.setter
    def org_customer_is_revoked(self, value):
        self._org_customer_is_revoked = value
    @property
    def org_customer_issue_date(self):
        return self._org_customer_issue_date

    @org_customer_issue_date.setter
    def org_customer_issue_date(self, value):
        self._org_customer_issue_date = value
    @property
    def org_customer_legal_person_cert_name(self):
        return self._org_customer_legal_person_cert_name

    @org_customer_legal_person_cert_name.setter
    def org_customer_legal_person_cert_name(self, value):
        self._org_customer_legal_person_cert_name = value
    @property
    def org_customer_legal_person_cert_no(self):
        return self._org_customer_legal_person_cert_no

    @org_customer_legal_person_cert_no.setter
    def org_customer_legal_person_cert_no(self, value):
        self._org_customer_legal_person_cert_no = value
    @property
    def org_customer_legal_person_cert_type(self):
        return self._org_customer_legal_person_cert_type

    @org_customer_legal_person_cert_type.setter
    def org_customer_legal_person_cert_type(self, value):
        self._org_customer_legal_person_cert_type = value
    @property
    def org_customer_legal_person_expire_date(self):
        return self._org_customer_legal_person_expire_date

    @org_customer_legal_person_expire_date.setter
    def org_customer_legal_person_expire_date(self, value):
        self._org_customer_legal_person_expire_date = value
    @property
    def org_customer_legal_person_pictures(self):
        return self._org_customer_legal_person_pictures

    @org_customer_legal_person_pictures.setter
    def org_customer_legal_person_pictures(self, value):
        if isinstance(value, list):
            self._org_customer_legal_person_pictures = list()
            for i in value:
                self._org_customer_legal_person_pictures.append(i)
    @property
    def org_customer_nature(self):
        return self._org_customer_nature

    @org_customer_nature.setter
    def org_customer_nature(self, value):
        self._org_customer_nature = value
    @property
    def org_customer_open_date(self):
        return self._org_customer_open_date

    @org_customer_open_date.setter
    def org_customer_open_date(self, value):
        self._org_customer_open_date = value
    @property
    def org_customer_pictures(self):
        return self._org_customer_pictures

    @org_customer_pictures.setter
    def org_customer_pictures(self, value):
        if isinstance(value, list):
            self._org_customer_pictures = list()
            for i in value:
                self._org_customer_pictures.append(i)
    @property
    def org_customer_registered_capital(self):
        return self._org_customer_registered_capital

    @org_customer_registered_capital.setter
    def org_customer_registered_capital(self, value):
        self._org_customer_registered_capital = value
    @property
    def org_customer_scope(self):
        return self._org_customer_scope

    @org_customer_scope.setter
    def org_customer_scope(self, value):
        self._org_customer_scope = value
    @property
    def person_customer_expire_date(self):
        return self._person_customer_expire_date

    @person_customer_expire_date.setter
    def person_customer_expire_date(self, value):
        self._person_customer_expire_date = value
    @property
    def person_customer_pictures(self):
        return self._person_customer_pictures

    @person_customer_pictures.setter
    def person_customer_pictures(self, value):
        if isinstance(value, list):
            self._person_customer_pictures = list()
            for i in value:
                self._person_customer_pictures.append(i)
    @property
    def person_user_expire_date(self):
        return self._person_user_expire_date

    @person_user_expire_date.setter
    def person_user_expire_date(self, value):
        self._person_user_expire_date = value
    @property
    def person_user_pictures(self):
        return self._person_user_pictures

    @person_user_pictures.setter
    def person_user_pictures(self, value):
        if isinstance(value, list):
            self._person_user_pictures = list()
            for i in value:
                self._person_user_pictures.append(i)
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_type(self):
        return self._user_type

    @user_type.setter
    def user_type(self, value):
        self._user_type = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserCertifyIdentifyInfoQueryResponse, self).parse_response_content(response_content)
        if 'cert_name' in response:
            self.cert_name = response['cert_name']
        if 'cert_no' in response:
            self.cert_no = response['cert_no']
        if 'cert_type' in response:
            self.cert_type = response['cert_type']
        if 'certify_grade' in response:
            self.certify_grade = response['certify_grade']
        if 'certify_time' in response:
            self.certify_time = response['certify_time']
        if 'havana_id' in response:
            self.havana_id = response['havana_id']
        if 'is_certified' in response:
            self.is_certified = response['is_certified']
        if 'is_released' in response:
            self.is_released = response['is_released']
        if 'logon_id' in response:
            self.logon_id = response['logon_id']
        if 'org_customer_expire_date' in response:
            self.org_customer_expire_date = response['org_customer_expire_date']
        if 'org_customer_is_cancelled' in response:
            self.org_customer_is_cancelled = response['org_customer_is_cancelled']
        if 'org_customer_is_exception' in response:
            self.org_customer_is_exception = response['org_customer_is_exception']
        if 'org_customer_is_in_black_list' in response:
            self.org_customer_is_in_black_list = response['org_customer_is_in_black_list']
        if 'org_customer_is_revoked' in response:
            self.org_customer_is_revoked = response['org_customer_is_revoked']
        if 'org_customer_issue_date' in response:
            self.org_customer_issue_date = response['org_customer_issue_date']
        if 'org_customer_legal_person_cert_name' in response:
            self.org_customer_legal_person_cert_name = response['org_customer_legal_person_cert_name']
        if 'org_customer_legal_person_cert_no' in response:
            self.org_customer_legal_person_cert_no = response['org_customer_legal_person_cert_no']
        if 'org_customer_legal_person_cert_type' in response:
            self.org_customer_legal_person_cert_type = response['org_customer_legal_person_cert_type']
        if 'org_customer_legal_person_expire_date' in response:
            self.org_customer_legal_person_expire_date = response['org_customer_legal_person_expire_date']
        if 'org_customer_legal_person_pictures' in response:
            self.org_customer_legal_person_pictures = response['org_customer_legal_person_pictures']
        if 'org_customer_nature' in response:
            self.org_customer_nature = response['org_customer_nature']
        if 'org_customer_open_date' in response:
            self.org_customer_open_date = response['org_customer_open_date']
        if 'org_customer_pictures' in response:
            self.org_customer_pictures = response['org_customer_pictures']
        if 'org_customer_registered_capital' in response:
            self.org_customer_registered_capital = response['org_customer_registered_capital']
        if 'org_customer_scope' in response:
            self.org_customer_scope = response['org_customer_scope']
        if 'person_customer_expire_date' in response:
            self.person_customer_expire_date = response['person_customer_expire_date']
        if 'person_customer_pictures' in response:
            self.person_customer_pictures = response['person_customer_pictures']
        if 'person_user_expire_date' in response:
            self.person_user_expire_date = response['person_user_expire_date']
        if 'person_user_pictures' in response:
            self.person_user_pictures = response['person_user_pictures']
        if 'user_id' in response:
            self.user_id = response['user_id']
        if 'user_type' in response:
            self.user_type = response['user_type']
