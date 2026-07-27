import React from 'react';

export const tableData = (
  <table>
    <tr>
      <th>Name</th>
    </tr>
    <tr>
      <td>Artorias</td>
    </tr>
    <tr>
      <td>Gwyn</td>
    </tr>
  </table>
);

export const renderingConstant = <h1>Loading HTML inside constant</h1>;
export const renderingWithBinding = <h1>The sum of 5 + 5 is {5 + 5}</h1>;
export const reactRenderingConstant = React.createElement('h1', {}, 'Basic usage!');