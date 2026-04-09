#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalDoctorinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalDoctorinfoQueryResponse, self).__init__()
        self._awards = None
        self._department_name = None
        self._doc_desc = None
        self._doctor_inner_id = None
        self._doctor_name = None
        self._organization = None
        self._skilled_desc = None
        self._title = None

    @property
    def awards(self):
        return self._awards

    @awards.setter
    def awards(self, value):
        self._awards = value
    @property
    def department_name(self):
        return self._department_name

    @department_name.setter
    def department_name(self, value):
        self._department_name = value
    @property
    def doc_desc(self):
        return self._doc_desc

    @doc_desc.setter
    def doc_desc(self, value):
        self._doc_desc = value
    @property
    def doctor_inner_id(self):
        return self._doctor_inner_id

    @doctor_inner_id.setter
    def doctor_inner_id(self, value):
        self._doctor_inner_id = value
    @property
    def doctor_name(self):
        return self._doctor_name

    @doctor_name.setter
    def doctor_name(self, value):
        self._doctor_name = value
    @property
    def organization(self):
        return self._organization

    @organization.setter
    def organization(self, value):
        self._organization = value
    @property
    def skilled_desc(self):
        return self._skilled_desc

    @skilled_desc.setter
    def skilled_desc(self, value):
        self._skilled_desc = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalDoctorinfoQueryResponse, self).parse_response_content(response_content)
        if 'awards' in response:
            self.awards = response['awards']
        if 'department_name' in response:
            self.department_name = response['department_name']
        if 'doc_desc' in response:
            self.doc_desc = response['doc_desc']
        if 'doctor_inner_id' in response:
            self.doctor_inner_id = response['doctor_inner_id']
        if 'doctor_name' in response:
            self.doctor_name = response['doctor_name']
        if 'organization' in response:
            self.organization = response['organization']
        if 'skilled_desc' in response:
            self.skilled_desc = response['skilled_desc']
        if 'title' in response:
            self.title = response['title']
