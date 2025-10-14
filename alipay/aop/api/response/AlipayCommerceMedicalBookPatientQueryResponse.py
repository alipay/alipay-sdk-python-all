#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalBookPatientQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalBookPatientQueryResponse, self).__init__()
        self._birth_date = None
        self._gender = None
        self._id_card_no = None
        self._id_card_type = None
        self._name = None
        self._patient_id = None
        self._phone_number = None
        self._relationship = None

    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value):
        self._birth_date = value
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value
    @property
    def id_card_no(self):
        return self._id_card_no

    @id_card_no.setter
    def id_card_no(self, value):
        self._id_card_no = value
    @property
    def id_card_type(self):
        return self._id_card_type

    @id_card_type.setter
    def id_card_type(self, value):
        self._id_card_type = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def patient_id(self):
        return self._patient_id

    @patient_id.setter
    def patient_id(self, value):
        self._patient_id = value
    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value
    @property
    def relationship(self):
        return self._relationship

    @relationship.setter
    def relationship(self, value):
        self._relationship = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalBookPatientQueryResponse, self).parse_response_content(response_content)
        if 'birth_date' in response:
            self.birth_date = response['birth_date']
        if 'gender' in response:
            self.gender = response['gender']
        if 'id_card_no' in response:
            self.id_card_no = response['id_card_no']
        if 'id_card_type' in response:
            self.id_card_type = response['id_card_type']
        if 'name' in response:
            self.name = response['name']
        if 'patient_id' in response:
            self.patient_id = response['patient_id']
        if 'phone_number' in response:
            self.phone_number = response['phone_number']
        if 'relationship' in response:
            self.relationship = response['relationship']
