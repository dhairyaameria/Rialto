import React from "react";

// components

import SalesForm from "components/Cards/SalesCard.js";

// layout for page

import Admin from "layouts/Admin.js";

export default function Settings() {
  return (
    <>
      <div className="flex flex-wrap">
        <div className="w-full px-4">
          <SalesForm />
        </div>
      </div>
    </>
  );
}

Settings.layout = Admin;